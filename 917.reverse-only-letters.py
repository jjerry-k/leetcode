#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
# Your runtime beats 98.58 % of python3 submissions
# Your memory usage beats 5.56 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars, idx, jdx = list(S), 0, len(S)-1
        while idx < jdx:
            while idx < jdx and not chars[idx].isalpha(): idx+=1
            while idx < jdx and not chars[jdx].isalpha(): jdx-=1
            chars[idx], chars[jdx] = chars[jdx], chars[idx]
            idx, jdx = idx + 1, jdx - 1
        return "".join(chars)
        
# @lc code=end