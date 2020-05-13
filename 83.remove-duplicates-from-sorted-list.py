#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
# Your runtime beats 19.7 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions (13.8 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head
# @lc code=end

