# 快速排序
times = 0


def qsort(l):
    global times
    times += 1
    if l == []:
        return []
    pivot = l[0]
    lesser = [i for i in l[1:] if i <= pivot]
    bigger = [i for i in l[1:] if i > pivot]
    lesser = qsort(lesser)
    bigger = qsort(bigger)
    return lesser + [pivot] + bigger


def get_pivot(nums, low, high):
    i=low
    j=high
    pivot=low
    # from end to start
    while(i<j):
        while nums[j]>=nums[pivot]:
            j-=1

        if i<j:
            nums[j], nums[pivot] = nums[pivot], nums[j]
            pivot = j

        while nums[i]<=nums[pivot]:
            i+=1

        if i<j:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            pivot = i

    return pivot

def qsort_2(nums, low, high):
    if low<high:
        pivot=get_pivot(nums, low, high)
        qsort_2(nums, low, pivot-1)
        qsort_2(nums, pivot+1, high)



def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low

def test_reference(array):
    array[0]=2500
    return array

def test_reference_no_return(array):
    array[0]=2500

def add_one(n):
    n+=1
    return n

def add_two(n):
    n+=2

l = [49, 38, 65, 97, 76, 13, 27, 49]

print("Raw: ", l)
print("Method 1: ", qsort(l))

qsort_2(l, 0, len(l)-1)
print("Method 2: ", l)

quick_sort_standord(l, 0, len(l)-1)
print("Method 3: ", l)

print("New array: ", test_reference(l))

a = [4,5,6,7,1]
test_reference_no_return(a)
print("new a: ", a)

d = 1522
print("add one: ", add_one(d))

d= 1522
add_two(d)
print(d)