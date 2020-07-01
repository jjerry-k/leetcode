#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
# Your runtime beats 58.54 % of python3 submissions
# Your memory usage beats 5.34 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        digit, char = [], []
        for elem in s:
            if elem.isdigit(): digit.append(elem)
            else: char.append(elem)
        
        if abs(len(digit)-len(char)) > 1 : return ""
        
        if len(digit) > len(char): return digit[0] + "".join([f"{c}{d}" for d, c in zip(digit[1:], char)]) 
        elif len(char) > len(digit): return char[0] + "".join([f"{d}{c}" for c, d in zip(char[1:], digit)]) 
        else: return "".join([f"{d}{c}" for c, d in zip(char, digit)])

# @lc code=end