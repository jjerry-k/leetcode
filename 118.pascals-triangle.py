#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
# Your runtime beats 67.97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            l = [0]+output[-1]
            r = output[-1]+[0]
            output.append([l[j]+r[j] for j in range(len(l))])
        return output[:numRows]

# @lc code=end