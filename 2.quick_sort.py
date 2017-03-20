# 快速排序

def qsort(l):
    if l == []:
        return []
    pivot = l[0]
    lesser = [i for i in l[1:] if i<=pivot]
    bigger = [i for i in l[1:] if i > pivot]
    lesser = qsort(lesser)
    bigger = qsort(bigger)
    return lesser + [pivot]+bigger

l = [4,53,34,56,67,54, 54]
print(qsort(l))