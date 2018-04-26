import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml

# own packages
from src.utils import Utils


class GDP():

    PATH = 'datafolder//raw//longlat//'
