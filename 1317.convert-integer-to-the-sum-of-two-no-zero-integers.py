#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
# Your runtime beats 80.98 % of python3 submissions
# Your memory usage beats 46.3 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for idx in range(n):
            if '0' not in f'{idx}{n-idx}':
                return [idx, n-idx]
# @lc code=end

