#!/bin/python3

import sys

def morganAndString(a, b):
    # Complete this function
    newList = []
    a = list(a)
    b = list(b)

    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            newList.append(a.pop(0))
        else:
            newList.append(b.pop(0))

    if len(a) == 0:
        newList = newList + b
    else:
        newList = newList + a

    newStr = "".join(newList)
    return newStr

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a = input().strip()
        b = input().strip()
        result = morganAndString(a, b)
        print(result)
