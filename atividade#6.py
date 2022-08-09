from collections import Counter

l1 = [5, 5, 1, 1, 9, 8, 1, 6, 2, 3]
l1.sort()
c = Counter(l1)
for i, cada in c.items():
    print(i, cada)
