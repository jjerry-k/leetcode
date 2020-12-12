#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
# Your runtime beats 69.89 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(",", ".")
# @lc code=end