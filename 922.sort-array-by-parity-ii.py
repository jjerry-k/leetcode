#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
# Your runtime beats 59.08 % of python3 submissions
# Your memory usage beats 54.71 % of python3 submissions (16.7 MB)
# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = [a for a in A if not a % 2], [a for a in A if a % 2]
        A[::2], A[1::2] = even, odd
        return A
# @lc code=end