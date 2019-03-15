import pickle

with open('./head-first-python/chapter4/mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1, 2, 'three'], mysavedata)

with open('./head-first-python/chapter4/mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)

print(a_list)


# sketch4 수정
man = []
other = []

try:
    data = open('./head-first-python/chapter4/sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()

            if role == 'man':
                man.append(line_spoken)
            elif role == 'other man':
                other.append(line_spoken)

        except ValueError:
            pass
    data.close()

except IOError as err:
    print("file error: " + str(err))

try:
    with open("./head-first-python/chapter4/man_data.txt", "wb") as man_file, open("./head-first-python/chapter4/other_data.txt", "wb") as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)

except IOError as err:
    print("file error: " + str(err))

except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))