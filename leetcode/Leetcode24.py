# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = pre = ListNode(0)
        pre.next = temp = head
        while temp != None:
            if temp.next !=None:
                pre.next = temp.next
                temp.next = pre.next.next
                pre.next.next = temp
            pre = temp
            temp = temp.next
        return res.next

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
s = Solution()
res = s.swapPairs(one)
while res != None:
    print(res.val)
    res = res.next