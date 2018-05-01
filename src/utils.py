
class Utils(object):

    states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
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
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming'}

    @classmethod
    def rename(cls, df):
        df.rename(columns=cls.states_dict, inplace=True)

        return df

    @staticmethod
    def read_states():
        with open('datafolder//columns.txt', 'r') as f:
            raw = f.read()
            contents = raw[:-1]  # to remove last space
            return contents.split('_')

    @classmethod
    def drop_cols(cls, df):

        states = cls.read_states()
        return df[states]

    @classmethod
    def test_states(cls):
        """
        Parameters
        ==========
        None


        Returns
        =======
        set_state1 : (set) states from dict
        set_state2 : (set) states from columns.txt


        """
        state_list = [cls.states_dict[key] for key in cls.states_dict]

        set_state1 = set(state_list)
        set_state2 = set(cls.read_states())

        return set_state1, set_state2
