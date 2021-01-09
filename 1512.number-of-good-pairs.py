#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
# Your runtime beats 14.92 % of python3 submissions
# Your memory usage beats 67.36 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return len([1 for idx in range(len(nums)-1) for sub_num in nums[idx+1:] if nums[idx] == sub_num])
# @lc code=end