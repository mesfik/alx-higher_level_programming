#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    Nstring = ""
    for c in str:
        if i == n:
            i += 1
            continue
        Nstring += c
        i += 1
    return Nstring
