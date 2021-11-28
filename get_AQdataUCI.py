from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import pandas as pd
import numpy as np

class Aq_from_uci():
    def __init__(self):
        self.aq_data = self.clean_aqdata()
    
    def open_url(self):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00360/AirQualityUCI.zip'
        resp = urlopen(url)
        return resp.read()
    
    def dwd_aqdata(self):
        # read zipfile
        urlfile = self.open_url()
        zipfile = ZipFile(BytesIO(urlfile))
        fname = 'AirQualityUCI.csv'
        airquality = pd.read_csv(zipfile.open(fname), sep=';', na_values = '-200')
        zipfile.close()
        return airquality
    
    def clean_aqdata(self):
        data = self.dwd_aqdata()
        #drop empty columns
        data.drop(data.iloc[:, 15:], inplace = True, axis = 1)
        data.drop('NMHC(GT)', inplace = True, axis = 1)
        data.dropna(how='all', inplace = True, axis = 0)
        
        #datetime column
        data['Date'] = pd.to_datetime(data['Date'], format = '%d/%m/%Y')
        
        # replace comma - dot as decimal !!!
        col_with_error = ['CO(GT)','C6H6(GT)', 'T', 'RH', 'AH']
        for col in col_with_error:
            data[col] = data[col].str.replace(',', '.').astype(float)
            data[col] = data[col].replace(-200.0, np.nan)

        return data
    
    def filter_aqdata(self, year = 2004):
        data = self.clean_aqdata()
        in_year = pd.DatetimeIndex(data['Date']).year == year
        data = data[in_year]
        return data
