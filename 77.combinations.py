#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
# Your runtime beats 72.57 % of python3 submissions
# Your memory usage beats 17 % of python3 submissions (15.5 MB)
# @lc code=start
class Solution:
    def combine(self, n: int, k: int):
        ch = [0] * (n+1)
        combination = []
        
        def DFS(s,combi):
            if len(combi) == k :
                combination.append(combi)
                return 
            else:
                for i in range(s,n+1):
                    DFS(i+1,combi+[i])
                        
        DFS(1,[])
        return combination
# @lc code=end

