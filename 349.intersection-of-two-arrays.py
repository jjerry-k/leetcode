#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
# Your runtime beats 55.47 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# @lc code=end

