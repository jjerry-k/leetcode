#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
# Your runtime beats 98.06 % of python3 submissions
# Your memory usage beats 25.52 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        for i in range(1, target[-1] + 1):
            result.append('Push')
            if i not in target:
                result.append('Pop')
        return result
# @lc code=end