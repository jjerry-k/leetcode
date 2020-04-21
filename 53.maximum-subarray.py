#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
# Your runtime beats 59.4 % of python3 submissions
# Your memory usage beats 5.69 % of python3 submissions (14.8 MB)

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
# @lc code=end

