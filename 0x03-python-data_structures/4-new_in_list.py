#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx < 0 or idx > length):
        return (my_list[idx])
    new_list = []
    for i in range(length):
        new_list.append(my_list[i])
    new_list.pop(idx)
    new_list.insert(idx, element)
    return (new_list)
