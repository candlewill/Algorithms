class Solution(object):
    result = []
    candidate_answer = []
    raw_target = 0

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.raw_target = target

        self.dfs(candidates, target, self.candidate_answer)
        return self.result

    def dfs(self, candidates, target, candidate_answer):
        sum_candidate = sum(self.candidate_answer)

        if sum_candidate==self.raw_target:
            self.result.append(candidate_answer)

        for c in candidates:
            self.candidate_answer.append(c)
            if sum(self.candidate_answer) == self.raw_target:
                self.result.append(self.candidate_answer)

            elif sum(self.candidate_answer) > self.raw_target:
                self.candidate_answer.pop()
                break

            else:
                target = target - c
                self.dfs(candidates, target, self.candidate_answer)


s = Solution()
candidates = [2, 3, 6, 7]
target = 7
result = s.combinationSum(candidates, target)
for r in result:
    print(r)
