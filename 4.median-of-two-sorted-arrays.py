#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1+nums2)
        length = len(new_list)
        if length%2 == 1:
            return new_list[length//2]
        else:
            half_length = length//2
            return (new_list[half_length-1] + new_list[half_length])/2
# @lc code=end

