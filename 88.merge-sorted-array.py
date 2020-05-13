#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
# Your runtime beats 67.34 % of python3 submissions
# Your memory usage beats 6.15 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()
# @lc code=end

