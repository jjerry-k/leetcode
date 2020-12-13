#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
# Your runtime beats 75.3 % of python3 submissions
# Your memory usage beats 49.39 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ["a"]*len(s)
        for i, val in enumerate(indices):
            result[val] = s[i]
        return "".join(result)
# @lc code=end