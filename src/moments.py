import numpy as np
import pandas as pd

#from prices import Prices
from src.gdp import GDP


class Moments(object):

    @staticmethod
    def home_skew(x):

        n = len(x)
        x_bar = np.mean(x)

        return 1 / n * np.sum((x - x_bar)**3)

    @staticmethod
    def home_kurtosis(x):

        n = len(x)
        x_bar = np.mean(x)

        return 1 / n * np.sum((x - x_bar)**4)

    @classmethod
    def moments(cls, data):

        mom1 = pd.Series(data.apply(np.mean, axis=1), name='mom1')
        mom2 = pd.Series(data.apply(np.std, axis=1), name='mom2')
        mom3 = pd.Series(data.apply(cls.home_skew, axis=1), name='mom3')
        mom4 = pd.Series(data.apply(cls.home_kurtosis, axis=1), name='mom4')

        return pd.concat([mom1, mom2, mom3, mom4], axis=1)
