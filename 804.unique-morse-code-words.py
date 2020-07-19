#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
# Your runtime beats 31.83 % of python3 submissions
# Your memory usage beats 80.38 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", 
            "--.", "....", "..", ".---", "-.-", ".-..", 
            "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", 
            "-.--", "--.."
            ]
        return len({''.join(morse[ord(i) - ord('a')] for i in w) for w in words})
# @lc code=end

