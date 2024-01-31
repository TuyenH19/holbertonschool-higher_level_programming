#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list.remove(my_list[len(my_list) - 1])
    return (my_list)
