# 二分查找

def bi_search_recursion(l, data):
    print('ok', l)
    if l[int(len(l) / 2)] == data:
        return True
    elif l[int(len(l) / 2)] < data:
        if len(l[int(len(l) / 2) + 1:]) == 0:
            return False
        return bi_search_recursion(l[int(len(l) / 2) + 1:], data)
    else:
        if len(l[:int(len(l) / 2)]) == 0:
            return False
        return bi_search_recursion(l[:int(len(l) / 2)], data)


def bi_search(l, data):
    left, right = 0, len(l) - 1
    while (left <= right):
        mid = int((left + right) / 2)
        if l[mid] == data:
            return True
        elif l[mid] < data:
            left = mid + 1
            print('有点小')
        elif l[mid] > data:
            right = mid - 1
            print('有点大')
    return False


l = [7, 3, 1, 67, 32.5, 65, 45]
print(sorted(l))
nb = 5
print(bi_search_recursion(sorted(l), nb))
print(bi_search(sorted(l), nb))
