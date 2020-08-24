#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
# Your runtime beats 84.6 % of python3 submissions
# Your memory usage beats 44.28 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        output = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                output.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in output])
        return output
# @lc code=end