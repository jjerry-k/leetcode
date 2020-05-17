#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
# Your runtime beats 94.02 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (15.2 MB)
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# @lc code=end