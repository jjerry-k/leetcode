#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
# Your runtime beats 64.68 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp_x = str(x)
        tmp_x_rev = ''.join(reversed(tmp_x))
        return tmp_x==tmp_x_rev
# @lc code=end

