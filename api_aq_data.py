from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import json
from get_AQdataUCI import *

app = Flask(__name__)
api = Api(app)

aq_data = Aq_from_uci()

class Dailymean(Resource):
    def get(self, year):
        aq_filtered = aq_data.filter_aqdata(year)
        
        #group by Day - Daily mean
        aq_daily = aq_filtered.groupby(['Date']).mean()
        
        #formatting to save
        lines = aq_daily.index.strftime('%d-%b-%Y')
        aq_daily = aq_daily.set_index(lines)
        #save
        filename = 'aq_daily_UCI_' + str(year)
        aq_daily.to_csv(filename + '.csv')
        aq_json = aq_daily.to_json()
        with open(filename + '.json', 'w') as f:
            json.dump(aq_json, f)
        #plot and save
        
        return aq_json

api.add_resource(Dailymean, '/year/<int:year>')

if __name__ == '__main__':
    app.run(debug=True)
