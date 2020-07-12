#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
# Your runtime beats 55.72 % of python3 submissions
# Your memory usage beats 72.77 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2str = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
            }
        if len(digits) == 0: return []
        elif len(digits) == 1: return [i for i in num2str[digits]]
        else:
            res = [i for i in num2str[digits[0]]]
            for digit in digits[1:]:
                res = [i+j for i in res for j in num2str[digit]]
            return res
        # @lc code=end