
class ColumnRenamer(object):
    
    def __init__(self, df):
        self.df = df
        
    def rename(self):
        self.df.rename(columns={
                'AK': 'Alaska',
                'AL': 'Alabama',
                'AZ': 'Arizona',
                'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'DE': 'Delaware',
                'FL': 'Florida',
                'GA': 'Georgia',
                'HI': 'Hawaii',
                'IA': 'Iowa',
                'ID': 'Idaho',
                'IL': 'Illinois',
                'IN': 'Indiana',
                'KS': 'Kansas',
                'KY': 'Kentucky',
                'LA': 'Louisiana',
                'ME': 'Maine',
                'MD': 'Maryland',
                'MA': 'Massachusetts',
                'MI': 'Michigan',
                'MN': 'Minnesota',
                'MS': 'Mississippi',
                'MO': 'Missouri',
                'MT': 'Montana',
                'NE': 'Nebraska',
                'NV': 'Nevada',
                'NH': 'New Hampshire',
                'NJ': 'New Jersey',
                'NM': 'New Mexico',
                'NY': 'New York',
                'NC': 'North Carolina',
                'ND': 'North Dakota',
                'OH': 'Ohio',
                'OK': 'Oklahoma',
                'OR': 'Oregon',
                'PA': 'Pennsylvania',
                'RI': 'Rhode Island',
                'SC': 'South Carolina',
                'SD': 'South Dakota',
                'TN': 'Tennesee',
                'TX': 'Texas',
                'UT': 'Utah',
                'VT': 'Vermont',
                'VA': 'Virginia',
                'WA': 'Washington',
                'WV': 'West Virginia',
                'WI': 'Wisconsin',
                'WY': 'Wyoming'}, inplace=True)
    
    def drop_cols(self):
        self.df.drop(['Alaska', 'Hawaii', 'Disctrict of Columbia'], axis=1)