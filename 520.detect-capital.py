#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
# Your runtime beats 98.05 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower():return True
        if word == word[0].upper()+word[1:].lower():return True
        if word == word.upper():return True
        return False
# @lc code=end

