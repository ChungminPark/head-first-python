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
    with open("./head-first-python/chapter4/man_data.out", "w") as man_file, open("./head-first-python/chapter4/other_data.out", "w") as other_file:
        print(man, file=man_file)
        print(other, file=other_file)

except IOError as err:
    print("file error: " + str(err))