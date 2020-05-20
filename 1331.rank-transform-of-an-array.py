#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
# Your runtime beats 8.7 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (39.3 MB)
# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dict = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return map(rank_dict.get, arr)
# @lc code=end