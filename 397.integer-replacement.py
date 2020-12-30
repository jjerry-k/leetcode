#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
# Your runtime beats 68.25 % of python3 submissions
# Your memory usage beats 69.01 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if not n % 2:
                n //= 2
            elif n % 4 == 1 or n==3 :
                n -= 1
            else:
                n += 1
            cnt += 1
        return cnt

# @lc code=end