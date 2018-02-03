def number_needed(a, b):
    from collections import Counter

    aCounter = Counter(a)
    bCounter = Counter(b)

    value1 = { k : bCounter[k] for k in set(bCounter) - set(aCounter) }
    value2 = { k : aCounter[k] for k in set(aCounter) - set(bCounter) }

    intersection = set(aCounter) & set(bCounter)
    aDifference = set(aCounter) - intersection
    bDifference = set(bCounter) - intersection

    # Difference counts for matching terms
    intersectionValues = { k : abs(aCounter[k] - bCounter[k]) for k in intersection}
    # Counts for non-matching terms
    aDifferenceValues = {k : aCounter[k] for k in aDifference}
    bDifferenceValues = {k : bCounter[k] for k in bDifference}

    intersectionSum = sum(intersectionValues.values())
    differenceSum = sum(aDifferenceValues.values()) + sum(bDifferenceValues.values())

    return intersectionSum + differenceSum

a = input().strip()
b = input().strip()

print(number_needed(a, b))
