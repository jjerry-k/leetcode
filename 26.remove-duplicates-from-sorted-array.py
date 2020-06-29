#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
# Your runtime beats 5.12 % of python3 submissions
# Your memory usage beats 7.38 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        cursor = 0
        while cursor < len(nums)-1:
            if nums[cursor] != nums[cursor+1]: 
                cursor += 1
                continue
            else : nums.pop(cursor)
            if len(nums) == len(set(nums)):break
        
# @lc code=end