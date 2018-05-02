import pandas as pd
import datetime
from src.utils import Utils

class Prices(object):
    
    PATH = 'datafolder//raw//salesprices//electricity.sas7bdat'
            
    @classmethod    
    def index_to_datetime(cls):
        df = pd.read_sas(cls.PATH)
        origin = datetime.datetime(1960, 1, 1).toordinal()
        for i in range(len(df)):
            df['date'][i] = datetime.datetime.fromordinal(int(df['date'][i]) + origin)
        pd.to_datetime(df.date)
        df = df.set_index('date')
        return df
        
    @classmethod
    def col_selector(cls):
        df = cls.index_to_datetime()
        prices = pd.DataFrame(index=df.index)
        for i in range(1, len(df.columns), 2):
                prices = pd.concat([prices, df.iloc[:, i]], axis=1)
        return prices
        
    
    @classmethod
    def col_names(cls):
        df = cls.col_selector()
        new_cols = [df.columns[i].split('_')[0] for i in range(len(df.columns))]
        df.columns = [new_cols]
        df = Utils.rename(df)
        df = Utils.drop_cols(df)
        return df
        
        
    @classmethod
    def clean_prices(cls):
        try: 
            df = cls.col_names()
            return df
        except:
            print('Process failed')
            
    
    @classmethod
    def write_sales(cls):
        df = cls.clean_prices()
        df.to_csv('datafolder//clean//prices.csv')

        