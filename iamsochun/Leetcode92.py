class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        hair = ListNode()
        hair.next = head
        before = hair
        for i in range(m - 1):
            before = before.next
        temp = ListNode()
        end = before.next
        for i in range(n - m + 1):
            now = before.next
            before.next = now.next
            now.next = temp.next
            temp.next = now
        end.next = before.next
        before.next = temp.next
        return hair.next

    def other(self, head: ListNode, m: int, n: int) -> ListNode:
        hair = ListNode()
        hair.next = head
        before = hair
        for i in range(m - 1):
            before = before.next
        now = before.next.next
        end = before.next
        for i in range(n - m):
            end.next = now.next
            now.next = before.next
            before.next = now
            now = end.next
        return hair.next
