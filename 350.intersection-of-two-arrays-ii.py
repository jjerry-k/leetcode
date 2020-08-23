#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
# Your runtime beats 33.1 % of python3 submissions
# Your memory usage beats 37.53 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return sum([[i]*min(nums1.count(i),nums2.count(i)) for i in set(nums1)&set(nums2)],[])
# @lc code=end