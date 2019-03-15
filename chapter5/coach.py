def sanitizer(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(spliter)
    return(mins + '.' + secs)

try:
    with open('./head-first-python/chapter5/james.txt') as james_data, open('./head-first-python/chapter5/julie.txt') as julie_data, open('./head-first-python/chapter5/mikey.txt') as mikey_data, open('./head-first-python/chapter5/sarah.txt') as sarah_data:
        
        james_data = james_data.readline()
        james = james_data.strip().split(',')
        julie_data = julie_data.readline()
        julie = julie_data.strip().split(',')
        mikey_data = mikey_data.readline()
        mikey = mikey_data.strip().split(',')
        sarah_data = sarah_data.readline()
        sarah = sarah_data.strip().split(',')

        james = sorted([sanitizer(each_t) for each_t in james])
        julie = sorted([sanitizer(each_t) for each_t in julie])
        mikey = sorted([sanitizer(each_t) for each_t in mikey])
        sarah = sorted([sanitizer(each_t) for each_t in sarah])

        unique_james = []
        for each in james:
            if each not in unique_james:
                unique_james.append(each)
        unique_julie = []
        for each in julie:
            if each not in unique_julie:
                unique_julie.append(each)
        unique_mikey = []
        for each in mikey:
            if each not in unique_mikey:
                unique_mikey.append(each)
        unique_sarah = []
        for each in sarah:
            if each not in unique_sarah:
                unique_sarah.append(each)

        print(unique_james[0:3])
        print(unique_mikey[0:3])
        print(unique_mikey[0:3])
        print(unique_sarah[0:3])
        
except FileNotFoundError as ferr:
    print('Error: ' + str(ferr))