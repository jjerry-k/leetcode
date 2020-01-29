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
        removed = []
        for i in nums: 
            if i not in removed :removed.append(i)
        print(nums)
        print(removed)
        nums = removed
        print(nums)
        return len(nums)
# @lc code=end



s = Solution()
print(s.removeDuplicates([1,1,2]))