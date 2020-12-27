#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
# Your runtime beats 21.5 % of python3 submissions
# Your memory usage beats 5.39 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
# @lc code=end