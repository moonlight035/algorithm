# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        before = head
        temp = head.next
        while temp:
            if temp.val == before.val:
                before.next = temp.next
            else:
                before = temp
            temp = temp.next
        return head