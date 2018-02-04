def ransom_note(magazine, ransom):
    from collections import Counter
    magazineCounter = Counter(magazine)
    ransomCounter = Counter(ransom)

    magazineCounter.subtract(ransomCounter)

    s = all(value >= 0 for value in magazineCounter.values())
    return s

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
