#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
# Your runtime beats 79.51 % of python3 submissions
# Your memory usage beats 67.25 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1])/len(salary[1:-1])
# @lc code=end