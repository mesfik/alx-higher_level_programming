#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2 != 0):
        upper = i - 32
        print("{}".format(chr(upper)), end='')
        continue
    print("{}".format(chr(i)), end='')
