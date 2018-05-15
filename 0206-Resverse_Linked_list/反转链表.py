# -*- coding: utf-8 -*-
# @Project : leetCode
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 反转链表.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        node = head
        pre = None
        while node is not None:
            nex = node.next
            node.next = pre
            pre = node
            node = nex
        return pre

class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        nex = head.next
        newHead = self.reverseList(nex)
        nex.next = head
        head.next = None
        return newHead
