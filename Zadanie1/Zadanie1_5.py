def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.union(set2))

def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

l1 = [1,2,4,8,16]
l2 = [2,4,6,8,10]

print(union(l1, l2))
print(intersection(l1, l2))