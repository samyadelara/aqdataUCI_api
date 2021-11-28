import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

class AQ_heatmap():

    @staticmethod
    def plot(year, dataframe: pd.DataFrame):
        corr = dataframe.corr()
        main = 'Air Quality Data (UCI) - Correlation Heatmap (' + str(year) + ')\n'
        
        plt.figure(figsize=(16, 6))
        heat_corr = sns.heatmap(
            corr, 
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 280, n=100),
            square=True
        )

        heat_corr.set_title(main,
                         fontdict = {'fontsize':16}, pad = 1)
        #save
        plt.savefig('AQ_heatmap.png', dpi=300, bbox_inches='tight', facecolor = 'white')
        
        return print('Plot done!')
