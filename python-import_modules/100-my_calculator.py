#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv

    x = argv[1]
    y = argv[3]
    o = argv[2]

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)
    elif (len(argv) == 4):
        if o == '+':
            print("{} {} {} = {}\n".format(x, o, y, add(int(x), int(y))))
            exit(0)
        elif o == '-':
            print("{} {} {} = {}\n".format(x, o, y, sub(int(x), int(y))))
            exit(0)
        elif o == '*':
            print("{} {} {} = {}\n".format(x, o, y, mul(int(x), int(y))))
            exit(0)
        elif o == '/':
            print("{} {} {} = {}\n".format(x, o, y, div(int(x), int(y))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /\n")
            exit(1)
