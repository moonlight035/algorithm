# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        hair = ListNode()
        hair.next = head
        end = hair
        temp = head
        while temp and temp.val < x:
            end = temp
            temp = temp.next
        before = end
        while temp:
            if temp.val < x:
                before.next = temp.next
                temp.next = end.next
                end.next = temp
                end = temp
                temp = before.next
            else:
                before = temp
                temp = temp.next
        return hair.next

s = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
s.partition(head,3)
