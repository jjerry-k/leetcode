#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
# Your runtime beats 78.24 % of python3 submissions
# Your memory usage beats 5.13 % of python3 submissions (14.2 MB)
# @lc code=start
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tmp = deque([x])
        tmp.extend(self.queue)
        self.queue = tmp
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# @lc code=end