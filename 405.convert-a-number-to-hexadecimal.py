#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
# Your runtime beats 36.62 % of python3 submissions
# Your memory usage beats 14.21 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def toHex(self, num):
        if num==0: return '0'
        mp = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            n = num & 15      
            hex = mp[n]         
            ans = hex + ans
            num = num >> 4
        return ans.lstrip('0')
# @lc code=end