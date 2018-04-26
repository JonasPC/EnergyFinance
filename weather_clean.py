import os
from urllib.request import urlretrieve
import pandas as pd
import datetime
from src.utils import Utils

class Weather(object):
    
    PATH = '..\\weather'
       
    @classmethod
    def load_weather(cls):
        os.chdir('weather')
        for i in range(1, 49):
            for j in range(1, 13):
                if os.path.exists('..\\' + str(i)+'-'+str(j)+'.csv') == True:
                    pass
                else:
                    URL = "https://www.ncdc.noaa.gov/cag/statewide/time-series/" \
                    + str(i) + "-tavg-1-" + str(j) + \
                    "-1990-2013.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000"
                    urlretrieve(URL, str(i)+'-'+str(j)+'.csv')
        os.chdir('..')
                    
    
    @staticmethod
    def clean_weather(data):
        weather = pd.DataFrame()
        monthly = pd.DataFrame()
        
        #Merging all datasets into something readable
        for j in range(1, 13):
            for i in range(1,49):
                df = pd.read_csv(str(i)+'-'+str(j)+'.csv', header=None)
                _state_name = df.iloc[0,0]
                df = df.iloc[4:,0:]
                df.columns = df.iloc[0,:]
                df.columns = ['time', str(_state_name), str(_state_name)]
                time_index = df.iloc[1:, 0]
                df = df.iloc[1:,1:]
                if i == 1:
                    monthly = pd.concat([monthly, time_index], axis=1)
                    monthly = pd.concat([monthly, df], axis=1)
                else:
                    monthly = pd.concat([monthly, df], axis=1)
            weather = pd.concat([weather, monthly], axis=0, ignore_index=True)
            monthly = pd.DataFrame()
    
    
        for i in range(len(weather)):
            weather.iloc[i, 0] = datetime.datetime.strptime(weather.iloc[i, 0], '%Y%m')
               
        weather = weather.sort_values(by='time')
        weather = weather.set_index('time')
            
        wea = pd.DataFrame(index=weather.index)
            
        if data == 'weather':
            for i in range(0, len(weather.columns), 2):
                wea = pd.concat([wea, weather.iloc[:, i]], axis=1)
        elif data == 'anomaly':
            for i in range(1, len(weather.columns), 2):
                wea = pd.concat([wea, weather.iloc[:, i]], axis=1)
        else:
            raise Exception('data must be "weather" or "anomaly"')
            
        wea = Utils.rename(wea)
        wea = Utils.drop_cols(wea)
        return wea
                
    def __repr__(self):
        return str(self.clean_weather('weather').head())
    
