#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
# Your runtime beats 13.67 % of python3 submissions
# Your memory usage beats 15.24 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        n_set = [i for i in range(1, n+1)] 
        for i, val in enumerate(itertools.permutations(n_set, n)):
            if i == k-1: return "".join([str(elem) for elem in val])
# @lc code=end