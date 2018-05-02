import pandas as pd
from src.moments import Moments

# own packagees
from src.utils import Utils


class DataRetrieve(object):

    CLEAN_PATH = 'datafolder//clean//'

    @classmethod
    def load_panel(cls, name):
        df = pd.read_csv(cls.CLEAN_PATH + name)
        df.set_index(pd.DatetimeIndex(df['time']), inplace=True)
        df.drop('time', axis=1, inplace=True)
        return df

    @classmethod
    def load_gdp(cls):
        return cls.load_panel('gdp.csv')

    @classmethod
    def load_weather(cls):
        return cls.load_panel('weather.csv')

    @classmethod
    def load_sales(cls):
        return cls.load_panel('sales.csv')

    @classmethod
    def load_prices(cls):
        return cls.load_panel('prices.csv')

    # Non Panel Data
    @classmethod
    def load_population(cls):
        df = pd.read_csv(cls.CLEAN_PATH + 'population.csv')
        df.set_index('Unnamed: 0', inplace=True)
        return df

    @classmethod
    def load_longlat(cls):
        df = pd.read_csv(cls.CLEAN_PATH + 'longlat.csv')
        df.set_index('Unnamed: 0', inplace=True)
        return df

    @classmethod
    def load_moments(cls):
        prices = cls.load_weather()
        return Moments.moments(prices)

    @classmethod
    def pick_state(cls, df, state):
        return df[state]

    @classmethod
    def state_data(cls, state):

        df_prices = pd.Series(cls.pick_state(cls.load_prices(), state), name='prices')
        df_sales = pd.Series(cls.pick_state(cls.load_sales(), state), name='sales')
        df_weather = pd.Series(cls.pick_state(cls.load_weather(), state), name='weather')

        return pd.concat([df_prices, df_sales, df_weather], axis=1)


DataRetrieve.state_data('Alabama').head()
