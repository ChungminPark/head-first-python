""" This is the standard way to include a multiple-line comment in your code."""

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idel"]]]

def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list) == True:
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                print("\t"*level, end='')
            print(each_item)

print_lol(movies, True)
