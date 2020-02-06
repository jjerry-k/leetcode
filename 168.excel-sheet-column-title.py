#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
# Your runtime beats 60.42 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i, j = divmod(n-1, 26)
        if i==0:
            return alphabet[j]
        else:
            return self.convertToTitle(i) + alphabet[j]
# @lc code=end

