#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
# Your runtime beats 98.26 % of python3 submissions
# Your memory usage beats 21.09 % of python3 submissions (17.9 MB)v
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_max = sum(nums[:k])
        tmp = curr_max
        for i in range(len(nums)-k):
            tmp = tmp - nums[i] + nums[i+k]
            if tmp > curr_max:
                curr_max = tmp
        return curr_max/k
# @lc code=end