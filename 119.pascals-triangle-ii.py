#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
# Your runtime beats 70.16 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for i in range(1, rowIndex+1):
            l = [0]+output[-1]
            r = output[-1]+[0]
            output.append([l[j]+r[j] for j in range(len(l))])
        return output[rowIndex]
# @lc code=end

