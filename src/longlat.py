import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml


class LongLat():

    def load_longlat():

        PATH = 'datafolder//raw//longlat//'

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

        pd.DataFrame(row_list, columns=row_header).to_csv(PATH + 'longlat.csv')
