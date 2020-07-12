#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
# Your runtime beats 82.45 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i in range(n)]
        result = 0
        for v in nums:
            result ^= v
        return result
# @lc code=end

