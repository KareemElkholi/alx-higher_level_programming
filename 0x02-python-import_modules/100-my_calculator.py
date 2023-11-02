#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        op = sys.argv[2]
        print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
