#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
# Your runtime beats 98.87 % of python3 submissions
# Your memory usage beats 19.13 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1, row_2, row_3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        output = []
        for word in words:
            elem = set(word.lower())
            if elem <= row_1 or elem <= row_2 or elem <= row_3:
                output.append(word)
        return output
        
# @lc code=end

