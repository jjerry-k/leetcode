#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)
# @lc code=end

