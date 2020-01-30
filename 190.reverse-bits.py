#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = n
        cnt = 32 - len(bin(tmp)[2:])
        tmp = ('0'* cnt + bin(tmp)[2:])[::-1]
        return int(tmp, 2)
# @lc code=end

