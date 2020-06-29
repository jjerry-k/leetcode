#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
# Your runtime beats 93.04 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (15.4 MB)
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a
# @lc code=end