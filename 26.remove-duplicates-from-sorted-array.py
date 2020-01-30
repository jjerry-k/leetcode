#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         to_set = list(set(nums))
#         print(to_set)
#         return len(to_set)
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