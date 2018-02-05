#!/bin/python3

import sys
from collections import Counter


def isValid(S):
    char_map = Counter(S)
    char_occurence_map = Counter(char_map.values())

    if len(char_occurence_map) == 1:
        return True

    if len(char_occurence_map) == 2:
        keys_list = list(char_occurence_map.keys())
        for key in char_occurence_map:
            if char_occurence_map[key] == 1 and (abs(keys_list[0] - keys_list[1]) == 1 or key == 1):
                return True

    return False


s = input().strip()
result = isValid(s)

if result:
    print("YES")
else:
    print("NO")
