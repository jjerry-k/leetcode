#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
# Your runtime beats 93.06 % of python3 submissions
# Your memory usage beats 6.38 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 15 ==0: result.append("FizzBuzz")
            elif i % 3 ==0: result.append("Fizz")
            elif i % 5 ==0: result.append("Buzz")
            else: result.append(str(i))
        return result
# @lc code=end