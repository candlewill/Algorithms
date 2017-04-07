'''Given an array and a value, remove all instances of that value in place and return the new length. The order of elements can be changed. It doesn't matter what you leave beyond the new length.'''


class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        j = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j + 1


s = Solution()
A = [4, 4, 3, 2, 4, 6, 5, 4]
elem = 4
length = s.removeElement(A, elem)
print(A)
print(length)
