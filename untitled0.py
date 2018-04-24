## pacakges
import os
import pandas as pd


## Loading data
os.chdir('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data')
gdp = pd.read_csv('gdp.csv', delimiter=',', index_col='Area')
gdp.index = pd.to_datetime(gdp.index)
pop = pd.read_csv('pop.csv', delimiter=',', index_col='Unnamed: 0')
pop.index = pd.to_datetime(pop.index)
wea = pd.read_csv('weather.csv', delimiter=';', index_col='time')
wea.index = pd.to_datetime(wea.index)
ano = pd.read_csv('ano.csv', delimiter=',', index_col='time')
ano.index = pd.to_datetime(ano.index)
lat = pd.read_csv('latitude.csv', delimiter=',', index_col='State')
pri = pd.read_csv('price.csv', delimiter=',', index_col='date') 
pri.index = pd.to_datetime(pri.index)
sal = pd.read_csv('sales.csv', delimiter=',', index_col='date') 
sal.index = pd.to_datetime(sal.index)


## Matching names
## Making func_create dataset

def column_matcher(df1, df2, df3, df4, df5, df6, df7):
    a, b, c, d, e, f, g = df1.columns, df2.columns, df3.columns, df4.columns, df5.columns, df6.columns, df7.columns
    return pd.DataFrame([a,b,c,d,e, f, g]).transpose()

test = column_matcher(gdp, lat, pri, sal, pop, wea, ano)
pri.columns = ['Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana','North Carolina', 'North Dakota', 'Nebraska', 'Hew Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
sal.columns = ['Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana','North Carolina', 'North Dakota', 'Nebraska', 'Hew Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']


new = [ano.columns[i].split('_')[0] for i in range(len(ano.columns))]
ano.columns = new
wea.columns = new
