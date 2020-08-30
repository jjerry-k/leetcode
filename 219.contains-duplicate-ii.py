#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
# Your runtime beats 78.94 % of python3 submissions
# Your memory usage beats 28.93 % of python3 submissions (21.6 MB)
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic and i <= dic[n]:
                return True
            dic[n] = i + k
        return False
# @lc code=end