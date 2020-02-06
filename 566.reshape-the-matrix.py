#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
# Your runtime beats 93.18 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = sum(nums, [])
        n = len(flatten)
        if r*c != n: return nums
        return [flatten[i:i+c] for i in range(0, n, c)]
# @lc code=end

