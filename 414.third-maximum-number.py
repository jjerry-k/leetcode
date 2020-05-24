#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
# Your runtime beats 72.64 % of python3 submissions
# Your memory usage beats 7.69 % of python3 submissions (15.2 MB)
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp =sorted(list(set(nums)))
        return tmp[-3] if len(tmp) >= 3 else tmp[-1]
# @lc code=end

