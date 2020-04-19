#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
# Your runtime beats 21.07 % of python3 submissions
# Your memory usage beats 5.55 % of python3 submissions (16.9 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        iterator = prehead.next
        prev = prehead
        
        while iterator is not None:
            if iterator.val == val:
                prev.next = iterator.next
            else:
                prev = iterator
            iterator = iterator.next
            
        return prehead.next
# @lc code=end

