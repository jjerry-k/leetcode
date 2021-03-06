#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
# Your runtime beats 77.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_1 = sum(distance[destination:start]) if start > destination else sum(distance[start:destination])
        sum_2 = sum(distance) - sum_1
        return min([sum_1, sum_2])

# @lc code=end