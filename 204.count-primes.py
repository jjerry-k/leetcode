#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
# Your runtime beats 85.21 % of python3 submissions
# Your memory usage beats 9.05 % of python3 submissions (44.8 MB)
# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0

        primes = [False, False] + [True] * (n - 2)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

# @lc code=end