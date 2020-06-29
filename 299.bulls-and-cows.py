#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
# Your runtime beats 94.88 % of python3 submissions
# Your memory usage beats 5.2 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = sum([i==j for i, j in zip(secret, guess)])
        B = sum([min(secret.count(i), guess.count(i)) for i in set(guess)])
        return f"{A}A{B-A}B"
# @lc code=end

