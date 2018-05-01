from src.longlat import LongLat


def write_states():
    with open('datafolder//columns.txt', 'w') as f:
        for state in list(LongLat.clean_longlat().columns):
            f.write('{}_'.format(state))
