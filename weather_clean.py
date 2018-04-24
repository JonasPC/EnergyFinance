import os
from urllib.request import urlretrieve
import pandas as pd
import datetime
os.chdir('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\weather')



## Downloading data from nddc.noaa.gov (governmental weather website)
for i in range(1, 49):
    for j in range(1, 13):
        if os.path.exists('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\weather\\' + str(i)+'-'+str(j)+'.csv') == True:
            pass
        else:
            URL = "https://www.ncdc.noaa.gov/cag/statewide/time-series/" + str(i) + "-tavg-1-" + str(j) +  "-1990-2013.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000"
            urlretrieve(URL, str(i)+'-'+str(j)+'.csv')
    

## Restructuring data s.t. it can be used for deep learning
weather = pd.DataFrame()
monthly = pd.DataFrame()

for j in range(1, 13):
    for i in range(1,49):
        df = pd.read_csv(str(i)+'-'+str(j)+'.csv', header=None)
        _temp = df.iloc[0,0]
        df = df.iloc[4:,0:]
        df.columns = df.iloc[0,:]
        df.columns = ['time', str(_temp) + '_Value' , str(_temp) + '_Anomaly' ]
        time_index = df.iloc[1:, 0]
        df = df.iloc[1:,1:]
        if i == 1:
            monthly = pd.concat([monthly, time_index], axis=1)
            monthly = pd.concat([monthly, df], axis=1)
        else:
            monthly = pd.concat([monthly, df], axis=1)
    weather = pd.concat([weather, monthly], axis=0, ignore_index=True)
    monthly = pd.DataFrame()

#weather['time_index'] = pd.to_datetime(weather.Date) 

for i in range(len(weather)):
   weather.iloc[i, 0] = datetime.datetime.strptime(weather.iloc[i, 0], '%Y%m')
   
weather = weather.sort_values(by='time')
weather = weather.set_index('time')

wea = pd.DataFrame(index=weather.index)
ano = pd.DataFrame(index=weather.index)
for i in range(len(weather.columns)):
    if i % 2 == 0:
        wea = pd.concat([wea, weather.iloc[:, i]], axis=1)
    else:
        ano = pd.concat([ano, weather.iloc[:, i]], axis=1)


wea.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\weather.csv', sep=';')
ano.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\ano.csv', sep=';')



