#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    Sum = 0
    for i in uniq_list:
        Sum += i
    return (Sum)
