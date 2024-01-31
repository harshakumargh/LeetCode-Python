from collections import Counter


class Solution:
    def findErrorNums(self, nums):
        rep , mis = None, None
        N = len(nums)
        lookup = Counter(nums)
        for i in range(1, N+1):
            if i not in lookup:
                mis = i
            if lookup[i] >1:
                rep = i
        return [rep,mis]


sln = Solution()
print(sln.findErrorNums([2,2]))