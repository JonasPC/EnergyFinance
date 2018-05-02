import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

# own packages
from src.utils import Utils


class GDP():

    @staticmethod
    def load_gdp(phase):
        """
        Parameters:
        ===========
        phase (string) : {'late', 'early'}

        Returns
        =======
        pd.DataFrame (object)
        """

        if phase is 'early':
            raw = pd.read_csv('datafolder//raw//gdp//gdp_early_period.csv', skiprows=4)
        elif phase is 'late':
            raw = pd.read_csv('datafolder//raw//gdp//gdp_late_period.csv', skiprows=4)
        else:
            raise ValueError('Phase must be either "late" or "early"')

        raw.rename(columns={'Area': 'time'}, inplace=True)
        raw.set_index('time', inplace=True)
        raw.drop('Fips', axis=1, inplace=True)
        raw = raw.transpose()
        raw.dropna(axis=1, inplace=True)

        raw = Utils.rename(raw)
        return Utils.drop_cols(raw)

    @classmethod
    def clean_gdp(cls):

        e_gdp = cls.load_gdp('early')
        l_gdp = cls.load_gdp('late')

        gdp = pd.concat([e_gdp, l_gdp])
        gdp['temptime'] = gdp.index
        gdp['time'] = gdp.apply(lambda row: datetime(int(row['temptime']), 1, 1), axis=1)
        gdp.set_index('time', inplace=True)

        gdp = gdp.resample('MS', label='left').mean().fillna(method='ffill')
        gdp = Utils.rename(gdp)
        return Utils.drop_cols(gdp)

    @classmethod
    def write_gdp(cls):
        df = cls.clean_gdp()
        df.to_csv('datafolder//clean//gdp.csv')


GDP.write_gdp()
