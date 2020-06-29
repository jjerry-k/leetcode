#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
# Your runtime beats 67.84 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return (len(A)==len(B)) and B in A*2
# @lc code=end

