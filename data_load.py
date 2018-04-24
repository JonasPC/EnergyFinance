import os
import pandas as pd
import datetime

os.chdir('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance')

data1 = pd.read_sas('electricity.sas7bdat')

for i in range(len(data1)):
    data1.date[i] = datetime.timedelta(days=data1.date[i]) + datetime.datetime.strptime('1960-01-01', '%Y-%m-%d')
data1.date = pd.to_datetime(data1.date)
data1 = data1.set_index('date')

price = pd.DataFrame(index=data1.index)
sales = pd.DataFrame(index=data1.index)

for i in range(len(data1)):
    if i % 2 == 0:
        sales = pd.concat([sales, data1.iloc[:, i]], axis=1)
    else:
        price = pd.concat([price, data1.iloc[:, i]], axis=1)

    

### GDP
data2 = pd.read_excel('state_gdp.xls')
data2 = data2.iloc[4:58, 1:]
data2 = data2.transpose()
data2.columns = data2.iloc[0, :]
data2 = data2.iloc[1:, :]
for i in range(len(data2)):
    data2.Area[i] = str(data2.Area[i])[0:4]
data2.Area = pd.to_datetime(data2.Area)
data2 = data2.set_index('Area')

data3 = pd.read_excel('state_gdp1990.xls')
data3 = data3.iloc[4:58, 1:]
data3 = data3.transpose()
data3.columns = data3.iloc[0, :]
data3 = data3.iloc[1:, :]
for i in range(len(data3)):
    data3.Area[i] = str(data3.Area[i])[0:4]
data3.Area = pd.to_datetime(data3.Area)
data3 = data3.set_index('Area')


databreak_converter = []
for i in range(len(data2.columns)):
    _converter = data2.iloc[0, i]/data3.iloc[-1, i]
    databreak_converter.append(_converter)

for i in range(len(data3)):
    for j in range((len(data3.columns))):
        data3.iloc[i, j] = data3.iloc[i, j]*databreak_converter[j]

data2 = data2.iloc[1:, :]

gdp = pd.concat([data3, data2], axis=0)

gdp.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\gdp.csv', sep=';') 
data1.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\electricity.csv', sep=';') 
price.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\price.csv', sep=';')
sales.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\sales.csv', sep=';')

lat = pd.read_csv('latitude.csv', delimiter=';', sep=',')
lat = lat.transpose()
lat.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\latitude.csv', sep=';') 

pop = pd.read_csv('population.csv', delimiter=';')
pop = pop.transpose()
pop.columns = pop.iloc[0, :]
pop = pop.iloc[1:, :]
pop.index = pd.to_datetime(pop.index)
pop = pop.sort_values(by='index')

pop.to_csv('C:\\Users\\Jonas\\OneDrive\\Dokumenter\\Økonomi_CSS\\8._semester\\Energy Finance\\clean data\\pop.csv', sep=';') 


