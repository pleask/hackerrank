#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    from collections import Counter

    arCount = Counter(ar)
    arMax = max(ar)

    return arCount(arMax)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
