# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = behind = head
        for i in range(n):
            behind = behind.next
        temp = None
        while behind != None:
            temp = pre
            pre = pre.next
            behind = behind.next
        if temp is None:
            return pre.next
        temp.next = pre.next
        return head