# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # [head,tail,remain] = self.reverseHead(head,k)
        # if remain!=None:
        #     tail.next = self.reverseKGroup(remain,k)
        # return head
        [pre,tail,remain] = self.reverseHead(head,k)
        res = pre
        while remain != None:
            [pre,next_tail,remain] = self.reverseHead(remain,k)
            tail.next = pre
            tail = next_tail
        return res


    def reverseHead(self, head: ListNode, k: int) -> [ListNode,ListNode]:
        temp = head
        length = 0
        while temp != None:
            length=length+1
            temp = temp.next
            if length==k:break
        if length<k:
            return [head,None,None]
        res = None
        temp = head
        while temp != None and k>0:
            x = temp
            temp = temp.next
            x.next = res
            res = x
            k = k-1
        return [res,head,temp]

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
one.next.next.next.next = ListNode(5)

s = Solution()
res = s.reverseKGroup(one,2)
while res != None:
    print(res.val)
    res = res.next