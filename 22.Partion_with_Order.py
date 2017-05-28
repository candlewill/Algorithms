# encoding: utf-8
import time

'''
Partition of a array according to negative and positive, keep the order of each part

For example,

Input: [5, -9, 4, 8, -6]
Output: [-9, -6, 5, 4, 8]
'''


def Partition_with_Order(arr):
    neg_idx, pos_idx = 0, len(arr) - 1
    while neg_idx <= pos_idx:
        while arr[neg_idx] < 0:
            neg_idx += 1
        while arr[pos_idx] >= 0:
            pos_idx -= 1
        if neg_idx > pos_idx:
            break

        arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]

    return arr

def Partition_with_Order_2(arr):
    import numpy as np
    arr = np.array(arr)
    pos_idx =  arr>=0
    neg_idx = arr<0
    return list(np.concatenate((arr[neg_idx], arr[pos_idx])))

def move_forward(arr):
    return [arr[-1]]+arr[:-1]

def Partition_with_Order_3(arr):
    firt_pos, right_neg = 0, 0
    while right_neg<=len(arr):
        while firt_pos<len(arr) and  arr[firt_pos]<=0:
            firt_pos+=1

        right_neg = firt_pos
        while right_neg<len(arr) and  arr[right_neg]>0:
            right_neg+=1

        if right_neg>=len(arr):
            break

        # arr[firt_pos], arr[right_neg] = arr[right_neg], arr[firt_pos]
        arr[firt_pos:right_neg + 1] = move_forward(arr[firt_pos:right_neg+1])

    return arr

def Partition_with_Order_4(arr):
    pos_result, neg_result = [a for a in arr if a>0], [a for a in arr if a<=0]
    return neg_result+pos_result



def main():
    input = [0,11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15]
    start_time = time.time()
    output = Partition_with_Order(input)
    print("--- %s seconds ---" % (time.time() - start_time))

    input = [0,11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9,
             -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15]
    start_time = time.time()
    output2 = Partition_with_Order_2(input)
    print("--- %s seconds ---" % (time.time() - start_time))

    input = [0,11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9,
             -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15]
    start_time = time.time()
    output3 = Partition_with_Order_3(input)
    print("--- %s seconds ---" % (time.time() - start_time))

    input = [0,11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9,
             -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15, 11, 7, -5, 9, -12, 15]
    start_time = time.time()
    output4 = Partition_with_Order_4(input)
    print("--- %s seconds ---" % (time.time() - start_time))

    print(output)
    print(output2)
    print(output3)
    print(output4)


if __name__ == '__main__':
    main()
