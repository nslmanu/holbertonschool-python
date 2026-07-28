#!/usr/bin/python3

def uppercase(str):
    for var in str:
        if ord(var) >= 97 and ord(var) <= 122:
            var = chr(ord(var) - 32)
        print("{}".format(var), end="")
    print("")
