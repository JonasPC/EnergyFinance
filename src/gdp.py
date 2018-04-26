import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml

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
        return pd.concat([e_gdp, l_gdp])
