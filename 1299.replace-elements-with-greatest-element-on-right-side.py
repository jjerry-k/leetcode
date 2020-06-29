#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
# Your runtime beats 76.86 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.3 MB)
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [-1]
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            max_val = max(max_val, arr[i])
            output.append(max_val)
        return output[::-1][1:]
# @lc code=end