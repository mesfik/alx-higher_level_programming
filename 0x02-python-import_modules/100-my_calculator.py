#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    oprator = sys.argv[2]
    if oprator == "+":
        print("{} {} {} = {}".format(a, oprator, b, add(a, b)))
    elif oprator == "-":
        print("{} {} {} = {}".format(a, oprator, b, sub(a, b)))
    elif oprator == "*":
        print("{} {} {} = {}".format(a, oprator, b, mul(a, b)))
    elif oprator == "/":
        print("{} {} {} = {}".format(a, oprator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
