import pickle
import file_nester

new_man = []

try:
    with open('./head-first-python/chapter4/man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

        file_nester.print_lol(new_man)
        print(new_man[0])
        print(new_man[-1])

except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

    