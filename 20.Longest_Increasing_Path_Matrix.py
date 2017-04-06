class Solution(object):
    width, height = 0, 0
    maxtrix = 0
    length = 0

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.maxtrix = matrix

        ans = 0
        for h in range(self.height):
            for w in range(self.width):
                print(h, w)
                self.length=1
                ans = max(ans, self.robot(h, w))

        return ans

    def robot(self, row, col):
        new_position = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
        for np in new_position:

            if np[1] < 0:
                continue
            if np[1] >= self.height:
                continue
            if np[0] < 0:
                continue
            if np[0] >= self.width:
                continue

            if self.maxtrix[np[0]][np[1]] > self.maxtrix[row][col]:
                self.length += 1
                self.robot(np[0], np[1])
        print(self.length)
        return self.length


s = Solution()
matrix1 = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

r1 = s.longestIncreasingPath(matrix1)
print(r1)

matrix2 = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

r2 = s.longestIncreasingPath(matrix2)
print(r2)
