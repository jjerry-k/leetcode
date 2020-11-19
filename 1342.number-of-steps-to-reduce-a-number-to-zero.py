#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
# Your runtime beats 77.72 % of python3 submissions
# Your memory usage beats 65.57 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # cnt = 0
        # while 1:
        #     if num == 0:
        #         return cnt
        #     elif num % 2 == 0:
        #         num /= 2
        #     else:
        #         num -= 1
        #     cnt += 1
        
        return len(bin(num)[2:])-1 + bin(num)[2:].count('1')
# @lc code=end