#!/bin/python3

import sys

def gradeHandler(grade):
    """
    Correct the individual grade.
    :param grade: int
    :return: int
    """
    if grade < 38:
        return grade

    mod = grade % 5
    if mod >= 3:
        return grade + (5 - (grade % 5))
    else:
        return grade

def solve(grades):
    correctedGrades = [gradeHandler(grade) for grade in grades]
    return correctedGrades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


