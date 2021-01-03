#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
# Your runtime beats 81.76 % of python3 submissions
# Your memory usage beats 19.44 % of python3 submissions (15.1 MB)
# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
# @lc code=end