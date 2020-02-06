#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
# ...? NameError: name 'convertToTitle' is not defined ...?

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i, j = divmod(n-1, 26)
        if i==0:
            return alphabet[j]
        else:
            return convertToTitle(i) + alphabet[j]
# @lc code=end

