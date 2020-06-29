#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
# Your runtime beats 92.32 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = n
        cnt = 32 - len(bin(tmp)[2:])
        tmp = ('0'* cnt + bin(tmp)[2:])[::-1]
        return int(tmp, 2)
# @lc code=end

