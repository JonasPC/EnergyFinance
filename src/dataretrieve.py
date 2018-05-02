import pandas as pd

# own packagees
from src.utils import Utils


class DataRetrieve(object):

    states = Utils.read_states()

    def data_for_state(state):
        assert state in cls.states, ""

    # cross sectional data
