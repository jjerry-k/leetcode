#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
# Your runtime beats 51.55 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i', 'o', 'u']
        s_list = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while s_list[i].lower() not in vowels and i < j: i += 1
            while s_list[j].lower() not in vowels and i < j: j -= 1
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i, j = i+1, j-1
        return ''.join(s_list)

# @lc code=end
    
