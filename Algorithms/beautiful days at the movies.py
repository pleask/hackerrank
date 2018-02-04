#!/bin/python3

import sys

def reverse(number):
    """
    :param number: An integer
    :return: The reverse of number
    """
    strNum = str(number)
    revStr = strNum[::-1]
    revNum = int(revStr)

    return revNum


def checkBeautiful(number, divisor):
    """
    Check whether abs(number - reverse(number)) % divisor = 0
    :param number: int
    :param divisor: int
    :return: boolean
    """
    return abs(number - reverse(number)) % divisor == 0

def beautifulDays(i, j, k):
    counter = 0
    for day in range(i, j + 1):
        if checkBeautiful(day, k):
            counter += 1
    return counter


if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
