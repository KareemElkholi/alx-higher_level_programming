#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    res = ""
    for x in range(x):
        try:
            res += str(my_list[x])
        except IndexError:
            break
    print(res)
    return len(res)
