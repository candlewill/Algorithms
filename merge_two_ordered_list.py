# 合并两个有序列表
# 知乎远程面试要求编程

def merge(l1, l2):
    i, j = 0, 0
    out = []
    while (i < len(l1) and j < len(l2)):
        if l1[i] <= l2[j]:
            out.append(l1[i])
            i += 1
        else:
            out.append(l2[j])
            j += 1
        if i == len(l1) or j == len(l2):
            out.extend(l1[i:])
            out.extend(l2[j:])
    return out


def recursion_merge(l1, l2, tmp=[]):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0]<l2[0]:
            tmp.append(l1[0])
            return recursion_merge(l1[1:], l2, tmp)
        else:
            tmp.append(l2[0])
            return recursion_merge(l1, l2[1:], tmp)



l1 = [4, 5, 8, 11, 22]
l2 = [5, 6, 8, 99, 121, 554]
print(merge(l1, l2))
print(recursion_merge(l1, l2, []))
