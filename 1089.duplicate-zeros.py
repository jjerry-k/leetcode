#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
# Your runtime beats 81.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
# @lc code=end

