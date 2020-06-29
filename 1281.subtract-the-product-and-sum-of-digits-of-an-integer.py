#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
# Your runtime beats 7.51 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = 0
        Prod = 1

        for i in str(n):
            Prod *= int(i)
            Sum += int(i)
        
        return Prod - Sum
# @lc code=end

