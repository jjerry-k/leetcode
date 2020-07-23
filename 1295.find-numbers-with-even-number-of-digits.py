#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
# Your runtime beats 5.25 % of python3 submissions
# Your memory usage beats 31.58 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(num)) % 2 == 0 for num in nums])
# @lc code=end