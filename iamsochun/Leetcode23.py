import math
from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i=0
        minPosition = -1
        minNode = None
        temp = res = ListNode(None)
        while i <= len(lists):
            if i == len(lists):
                if minNode == None:
                    break
                else:
                    temp.next = minNode
                    lists[minPosition] = minNode.next
                    i = 0
                    temp = temp.next
                    minNode = None
                    minPosition = -1
            if lists[i] != None and (minNode == None or minNode.val > lists[i].val):
                minPosition = i
                minNode = lists[i]
            i = i+1
        return res.next
    def other(self, lists:List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists)==1:
            return lists[0]
        mid = len(lists)//2
        left = lists[0:mid]
        right = lists[mid:len(lists)]
        left_res = self.other(left)
        right_res = self.other(right)
        return self.mergeTwoLists(left_res,right_res)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = res = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 != None else l2
        return res.next


one = ListNode(1)
one.next = ListNode(4)
one.next.next = ListNode(5)

two = ListNode(1)
two.next = ListNode(3)
two.next.next = ListNode(4)

three = ListNode(2)
three.next = ListNode(6)
s = Solution()
res = s.other([one,two,three])
while res != None:
    print(res.val)
    res = res.next