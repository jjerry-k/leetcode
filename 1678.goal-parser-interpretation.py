#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
# Your runtime beats 63.28 % of python3 submissions
# Your memory usage beats 43.32 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace(f"()", "o")
        command = command.replace(f"(", "")
        command = command.replace(f")", "")
        return command
# @lc code=end