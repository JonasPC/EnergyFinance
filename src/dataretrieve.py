import pandas as pd
from src.moments import Moments
from src.utils import Utils

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
    def load_moments(cls, mom_nr):
        """
        Parameter
        =========
        mom_nr (int) : {1, 2, 3, 4} a given momen wanted to be returned


        Returns
        =======
        Moment of sales (pd.Series)
        """

        moments_dict = {1: 'mom1', 2: 'mom2', 3: 'mom3', 4: 'mom4'}
        prices = cls.load_prices()
        moments = Moments.moments(prices)
        return pd.Series(moments[moments_dict[mom_nr]])

    @classmethod
    def pick_state(cls, df, state):
        return df[state]

    @classmethod
    def former_obs(cls, state, series_name):
        """
        Parameter
        =========
        state (str) : name of string
        series_name (str) : {'prices' , 'sales', 'weather'}

        Returns
        =======
        pd.DataFrame (object)
        """
        load_dict = {'prices': cls.load_prices(),
                     'sales': cls.load_sales(),
                     'weather': cls.load_weather(),
                     'mom1': cls.load_moments(1),
                     'mom2': cls.load_moments(2),
                     'mom3': cls.load_moments(3),
                     'mom4': cls.load_moments(4)}

        if series_name in ['mom1', 'mom2', 'mom3', 'mom4']:
            series_t = pd.Series(load_dict[series_name])

        elif series_name in ['prices', 'sales', 'weather']:
            series_t = pd.Series(cls.pick_state(load_dict[series_name], state), name=series_name)

        else:
            raise ValueError('series_name not a possibility')

        series_t1 = pd.Series(series_t.shift(1), name='{}_t1'.format(series_name))
        series_t2 = pd.Series(series_t.shift(2), name='{}_t2'.format(series_name))

        return pd.concat([series_t, series_t1, series_t2], axis=1)

    @classmethod
    def cross_var_state(cls, state, var):
        """ Cross sectional variable by state

        Method used to get a state specific longitude, latitude or population

        Parameters
        ==========
        state (str) : string with state name
        var (str) : {'longitude', 'latitude', 'population'}

        Returns
        =======
        value (float) : value of given state specific variable
        """

        var_dict = {'longitude': 'Longitude',
                    'latitude': 'Latitude', 'population': 'POPESTIMATE2017'}

        if var in ['longitude', 'latitude']:
            df = cls.load_longlat()
            return float(df.loc[df.index == var_dict[var]][state])

        elif var in ['population']:
            df = cls.load_population()
            return int(df[state])

    @classmethod
    def state_data(cls, state):

        prices = cls.former_obs(state=state, series_name='prices')
        sales = cls.former_obs(state=state, series_name='sales')
        weather = cls.former_obs(state=state, series_name='sales')

        mom1 = cls.former_obs(state=state, series_name='mom1')
        mom2 = cls.former_obs(state=state, series_name='mom2')
        mom3 = cls.former_obs(state=state, series_name='mom3')
        mom4 = cls.former_obs(state=state, series_name='mom4')

        gdp = pd.Series(cls.pick_state(cls.load_gdp(), state), name='gdp')

        df = pd.concat([prices, sales, weather, gdp, mom1, mom2, mom3, mom4], axis=1)

        df['population'] = cls.cross_var_state(state=state, var='population')
        df['longitude'] = cls.cross_var_state(state=state, var='longitude')
        df['latitude'] = cls.cross_var_state(state=state, var='latitude')
        df['month'] = df.index.month
        df['year'] = df.index.year

        df['y'] = df['prices'].shift(-1)

        return df.dropna(axis=0)


DataRetrieve.state_data('Alabama')
