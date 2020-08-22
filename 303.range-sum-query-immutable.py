#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
# Your runtime beats 22.76 % of python3 submissions
# Your memory usage beats 71.34 % of python3 submissions (17.3 MB)
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end