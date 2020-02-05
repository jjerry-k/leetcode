#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
# Your runtime beats 83.07 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[nums[i]] + j for i in range(len(nums)) for j in self.permute(nums[:i]+nums[i+1:])] or [[]]
# @lc code=end