from scipy.stats import moment
#moment([1, 2, 3, 4, 5], moment=1)

#from prices import Prices
from src.gdp import GDP


class Moments(object):

    @staticmethod
    def moments(data):
        df = data.apply(moment, axis=1)
        return df


data = GDP.clean_gdp()
data.head()

moment([-1, 2, 2, 3], axis=0, moment=1)


def moment_func(x, power):
    """
    x : (array like) vector
    power : (int)
    """
    n = len(data)
    x_bar = np.mean(x)
