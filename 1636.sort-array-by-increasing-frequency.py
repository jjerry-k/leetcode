#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
# Your runtime beats 32.04 % of python3 submissions
# Your memory usage beats 19.04 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count_dict = {i:nums.count(i) for i in set(nums)}
        return sorted(nums, key=lambda x: (count_dict[x], -x))
# @lc code=end