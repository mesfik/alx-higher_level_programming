#!/usr/bin/python3
import math
for i in range(99):
    last_digit = i % 10
    num = math.floor(i / 10)
    print("{:.0f}{:.0f}".format(num, last_digit), end=", ")
print("99")
