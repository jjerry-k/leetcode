#
# @lc app=leetcode id=1668 lang=python3
#
# [1668] Maximum Repeating Substring
# Your runtime beats 87.3 % of python3 submissions
# Your memory usage beats 47.1 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        return sum(word * i in sequence for i in range(1, 101))
# @lc code=end