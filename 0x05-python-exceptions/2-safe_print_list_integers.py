#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    indx = 0

    for i in range(x):

        try:
            print("{}".format(my_list[i]), end="")
            indx += 1
        except(ValueError, TypeError):
            break
    print()

    return indx
