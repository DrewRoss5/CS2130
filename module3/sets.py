def intersection_of_sets(set1, set2):
    intersect = []
    for i in set1:
        if i in set2:
            intersect.append(i)
    intersect.sort()
    return intersect


def union_of_sets(set1, set2):
    for i in set1:
        if i not in set2:
            set2.append(i)
    set2.sort()
    return set2

