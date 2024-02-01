#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if print("{:d}".format(element)) == True:
                print(element)
                count += 1
            if count == x:
                break
    except IndexError:
        return (False)
    print('')
    return (x - not_int)
