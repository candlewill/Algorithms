class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > answer:
                    answer = sum
        return answer

    def greedy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]
        sum = 0
        for num in nums:
            sum += num
            answer = max(answer, sum)
            sum = max(sum, 0)
        return answer

    # Wrong
    def max_min(self, nums):
        sum = 0
        max_nb, min_nb = nums[0], nums[0]
        for num in nums:
            sum += num
            max_nb = max(max_nb, sum)
            min_nb = min(min_nb, sum)

        return max_nb - min_nb

    # wrong
    def max_minother(self, nums):
        sum = 0
        max_nb, min_nb = nums[0], nums[0]
        max_index, min_index = 0, 0
        for num in nums:
            sum += num
            # max_nb = max(max_nb, sum)
            while max_index >= min_index:
                if max_nb < sum:
                    max_nb = sum
                    max_index = num
                if min_nb > sum:
                    min_nb = sum
                    min_index = num

                    # min_nb = min(min_nb, sum)

        return max_nb - min_nb

    def sum_sub(self, nums):
        s = nums
        for i in range(1, len(nums)):
            s[i] += s[i - 1]

        max_value = s[0]
        for j in range(len(nums)):
            min_value = 0
            for i in range(0, j):
                min_value = min(min_value, s[i])

            max_value = max(max_value, s[j] - min_value)

        return max_value

    def sum_sub_optimised(self, nums):
        max_value = nums[0]
        min_value = 0
        sj = 0
        si = 0
        for j in range(len(nums)):
            sj += nums[j]
            min_value = min(si, min_value)
            max_value = max(max_value, sj - min_value)
            si += nums[j]

        return max_value


nums = [-2, -1]
s = Solution()
print(s.maxSubArray(nums))
print(s.greedy(nums))
print(s.max_min(nums))
# print(s.max_minother(nums))
print(s.sum_sub(nums))

nums = [-2, -1, -4]
print(s.sum_sub_optimised(nums))
