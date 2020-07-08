#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
# Your runtime beats 6.78 % of python3 submissions
# Your memory usage beats 38.64 % of python3 submissions (13.9 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cnt = 0
        new_node = ListNode(0)
        new_node.next = head
        cur_node = new_node
        while cur_node.next and cur_node.next.next:
            node_1, node_2 = cur_node.next, cur_node.next.next
            cur_node.next = node_2
            node_1.next = node_2.next
            node_2.next = node_1
            cur_node = cur_node.next.next
        return new_node.next            

# @lc code=end