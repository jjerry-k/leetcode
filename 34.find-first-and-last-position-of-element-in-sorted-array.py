#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
# Your runtime beats 70.27 % of python3 submissions
# Your memory usage beats 5.36 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target)==0 : return [-1, -1]
        return [nums.index(target), len(nums)-1-nums[::-1].index(target)]
# @lc code=end

