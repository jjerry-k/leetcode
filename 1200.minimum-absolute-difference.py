#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_val = min(j - i for i, j in zip(arr[:-1], arr[1:]))
        result = [[i, j] for i, j in zip(arr[:-1], arr[1:]) if j-i==min_val]
        return result
# @lc code=end

