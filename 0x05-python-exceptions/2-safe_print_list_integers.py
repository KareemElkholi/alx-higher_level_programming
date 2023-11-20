def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for x in range(x):
        try:
            print("{:d}".format(int(my_list[x])), end="")
            length += 1
        except (ValueError, TypeError):
            continue
    print("")
    return length
