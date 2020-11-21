#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
# Your runtime beats 84.05 % of python3 submissions
# Your memory usage beats 31.89 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_pow = []
        i = 0
        while 1:
            if x==1: 
                x_pow.append(1)
                break
            tmp = x**i
            if tmp <= bound: x_pow.append(tmp)
            else: break
            i+=1
        
        y_pow = []
        i = 0
        while 1:
            if y==1: 
                y_pow.append(1)
                break
            tmp = y**i
            if tmp <= bound: y_pow.append(tmp)
            else: break
            i+=1

        return list(set([x_tmp + y_tmp for x_tmp in x_pow for y_tmp in y_pow if x_tmp + y_tmp <= bound]))
# @lc code=end