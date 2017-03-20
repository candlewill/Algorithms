def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    mid = int((m + n) / 2)
    out = 0
    i, j = 0, 0
    for k in range(mid):
        if i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
                out = nums1[i]
            else:
                j += 1
                out = nums2[j]
        elif i >= m:
            j += 1
            out = nums2[j]
        else:
            i += 1
            out = nums1[i]
    return out


a = [4,5,7,9,22]
b = [5,6,9,121,3345]
print(findMedianSortedArrays(a,b))