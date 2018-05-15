# -*- coding: utf-8 -*-
# @Project : leetCode
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 环形链表.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next_=None):
        self.val = x
        self.next = next_


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slower = quicker = head

        while slower is not None and quicker is not None:
            slower = slower.next
            quicker = quicker.next
            if quicker is not None:
                quicker = quicker.next
            if slower is quicker:
                return True
        return False


solution = Solution()
l = ListNode([1], ListNode([2]))
res = solution.hasCycle(l)
print(res)
