import pandas as pd
import requests
from urllib.request import urlretrieve

# own packages
from src.utils import Utils


class Population():

    PATH = 'datafolder//raw//population//'
    URL = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/state/asrh/scprc-est2017-18+pop-res.csv'

    @classmethod
    def load_population(cls):

        urlretrieve(cls.URL, cls.PATH + 'Population.csv')

    @classmethod
    def to_clean(cls):

        raw = pd.read_csv(cls.PATH + 'Population.csv', encoding='latin-1')
        cols = raw.drop([0])['NAME']
        pop = raw.drop([0])['POPESTIMATE2017']

        df = pd.DataFrame([pop])
        df.columns = cols
        return df

    @classmethod
    def clean_population(cls):

        try:
            df = cls.to_clean()

        except:

            print('in exception')

            cls.load_population()
            df = cls.to_clean()

        df = Utils.rename(df)
        return Utils.drop_cols(df)

    @classmethod
    def write_population(cls):

        df = cls.clean_population()
        df.to_csv('datafolder//clean//population.csv')
