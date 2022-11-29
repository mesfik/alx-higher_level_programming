#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        isupper = ord(ch) >= ord('a') and ord(ch) <= ord('z')
        if isupper:
            diff = ord('A') - ord('a')
            ch = chr(ord(ch) + diff)
        print("{}".format(ch), end='')
    print()
