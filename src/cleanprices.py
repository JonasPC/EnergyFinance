import pandas as pd
import datetime
from src.utils import Utils

class CleanPrices(object):
    
    def __init__(self, path):
        self.path = path
        self.data = pd.read_sas(path)
        
    def __repr__(self):
        return str(self.data.head())
        
    def step_1(self):
        for i in range(len(self.data)):
            self.data['date'][i] = datetime.timedelta(days=self.data['date'][i]) + \
            datetime.datetime.strptime('1960-01-01', '%Y-%m-%d')
        pd.to_datetime(self.data.date)
        self.data = self.data.set_index('date')
        
        
    def step_2(self):
        price = pd.DataFrame(index=self.data.index)
        for i in range(1, len(self.data.columns), 2):
                price = pd.concat([price, self.data.iloc[:, i]], axis=1)
        self.data = price
    
    def step_3(self):
        new_cols = [self.data.columns[i].split('_')[0] for i in range(len(self.data.columns))]
        self.data.columns = [new_cols]
        self.data = Utils.rename(self.data)
        self.data = Utils.drop_cols(self.data)
  
    
class CleanSales(object):
    
    def __init__(self, path):
        self.path = path
        self.data = pd.read_sas(path)
        
    def __repr__(self):
        return str(self.data.head())
        
    def step_1(self):
        for i in range(len(self.data)):
            self.data['date'][i] = datetime.timedelta(days=self.data['date'][i]) + \
            datetime.datetime.strptime('1960-01-01', '%Y-%m-%d')
        pd.to_datetime(self.data.date)
        self.data = self.data.set_index('date')
        
        
    def step_2(self):
        sales = pd.DataFrame(index=self.data.index)
        for i in range(0, len(self.data.columns), 2):
                sales = pd.concat([sales, self.data.iloc[:, i]], axis=1)
        self.data = sales
    
    def step_3(self):
        new_cols = [self.data.columns[i].split('_')[0] for i in range(len(self.data.columns))]
        self.data.columns = [new_cols]
        self.data = Utils.rename(self.data)
        self.data = Utils.drop_cols(self.data)
        