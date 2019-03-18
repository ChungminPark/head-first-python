import pickle
from .athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')

            return AthleteList(templ.pop(0), templ.pop(0), templ)

    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


def put_to_store(files_list):
    all_athletes = {}

    for file in files_list:
        ath = get_coach_data(file)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athlete = {}

    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return all_athlete


the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
for each_athlete in data:
    print(data[each_athlete].name + ' ' + data[each_athlete].dob)

data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)