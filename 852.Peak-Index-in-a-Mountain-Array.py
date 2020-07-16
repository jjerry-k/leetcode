# Runtime: 76 ms, faster than 88.04% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 15 MB, less than 58.11% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
