#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
# Your runtime beats 30.71 % of python3 submissions
# Your memory usage beats 89.34 % of python3 submissions (14.9 MB)
# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
# @lc code=end

