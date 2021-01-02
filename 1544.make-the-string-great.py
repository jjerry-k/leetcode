#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
# Your runtime beats 62.64 % of python3 submissions
# Your memory usage beats 11.07 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for c in s: 
            if res and ord(res[-1]) ^ ord(c) == 32: res.pop()
            else: res.append(c)
        return "".join(res)
# @lc code=end