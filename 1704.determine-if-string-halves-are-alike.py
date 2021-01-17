#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
# Your runtime beats 38.5 % of python3 submissions
# Your memory usage beats 68.73 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u"]
        half = len(s)//2
        first_half = [s[:half].lower().count(vowel) for vowel in vowels]
        second_half = [s[half:].lower().count(vowel) for vowel in vowels]
        return sum(first_half) == sum(second_half)
# @lc code=end