#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    arrSum = sum(arr)

    min4 = arrSum - max(arr)
    max4 = arrSum - min(arr)

    print(min4, max4)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
