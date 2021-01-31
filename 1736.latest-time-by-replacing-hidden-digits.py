#
# @lc app=leetcode id=1736 lang=python3
#
# [1736] Latest Time by Replacing Hidden Digits
# Your runtime beats 91.85 % of python3 submissions
# Your memory usage beats 57.81 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        string = list(time)
        for i in range(len(string)):
            if string[i] == "?": 
                if i==0: string[i] = "2" if string[i+1] in "?0123" else "1"
                elif i==1: string[i] = "9" if string[0] in "01" else "3"
                elif i==3: string[i] = "5"
                else: string[i] = "9"
        return "".join(string)
# @lc code=end