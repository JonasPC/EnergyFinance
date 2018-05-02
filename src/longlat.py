import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml

# own packages
from src.utils import Utils


class LongLat():

    PATH = 'datafolder//raw//longlat//'

    @classmethod
    def load_longlat(cls):

        source = requests.get('https://inkplant.com//code//state-latitudes-longitudes').text
        soup = BeautifulSoup(source, 'lxml')

        table = soup.find('table')  # finding table in HTML soup
        table_rows = table.find_all('tr')  # finding all table rows, s.t. one can loop over them

        row_list = list()

        # looping to create dataframe
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            if row[0] == 'State':
                row_header = row
            else:
                row_list.append(row)

        pd.DataFrame(row_list, columns=row_header).to_csv(cls.PATH + 'longlat.csv', index=False)

    @classmethod
    def clean_longlat(cls):

        #df_test = pd.read_csv(cls.PATH + 'longlat.csv')
        try:
            df = pd.read_csv(cls.PATH + 'longlat.csv')
            df = df.set_index('State').transpose()

        except:

            print('in exception')
            cls.load_longlat()
            df = pd.read_csv(cls.PATH + 'longlat.csv')
            df = df.set_index('State').transpose()

        df = Utils.rename(df)
        return Utils.drop_cols(df)

    @classmethod
    def write_longlat(cls):
        df = cls.clean_longlat()
        df.to_csv('datafolder//clean//longlat.csv')