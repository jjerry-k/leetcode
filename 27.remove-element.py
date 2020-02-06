#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
# Your runtime beats 10.74 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)
# @lc code=end

