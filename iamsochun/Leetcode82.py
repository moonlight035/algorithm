# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        end = hair = ListNode(0)
        temp = head
        while temp:
            if not temp.next or temp.next.val != temp.val:
                end.next = temp
                end = temp
                temp = temp.next
                end.next = None
            else:
                while temp.next and temp.next.val == temp.val:
                    temp = temp.next
                temp = temp.next
        return hair.next

s = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(2)

one.next = two
two.next = three
print(s.deleteDuplicates(one))



