def number_needed(a, b):
    from collections import Counter

    aCounter = Counter(a)
    bCounter = Counter(b)

    aCounter.subtract(bCounter)

    swaps = sum([abs(i) for i in aCounter.values()])

    return swaps

a = input().strip()
b = input().strip()

print(number_needed(a, b))
