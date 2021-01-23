#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
# Your runtime beats 71.71 % of python3 submissions
# Your memory usage beats 37.21 % of python3 submissions (17.3 MB)
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
# @lc code=end