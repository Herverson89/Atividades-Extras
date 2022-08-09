l1 = [5, 5, 1, 1, 9, 8, 1, 6, 2, 3]
l2 = []
c = l1.count(l2)
rep = 0
for x in l1:
    if x not in l2:
        l2.append(x)
    l2.sort()
print(l2)
