#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
# Your runtime beats 56.05 % of python3 submissions
# Your memory usage beats 5.97 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

# @lc code=end