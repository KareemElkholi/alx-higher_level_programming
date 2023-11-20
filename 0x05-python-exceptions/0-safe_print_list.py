#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for x in range(x):
        try:
            print(my_list[x], end='')
            length += 1
        except IndexError:
            break
    print("")
    return length
