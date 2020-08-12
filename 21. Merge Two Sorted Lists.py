class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = p = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next

mm = Solution()
head = ListNode(None)
cur = head
for i in [1,2,4]:
    cur.next = ListNode(i)
    cur = cur.next
head1 = head.next
head = ListNode(None)
cur = head
for i in [1,3,4]:
    cur.next = ListNode(i)
    cur = cur.next
head2 = head.next

res = mm.mergeTwoLists(head1, head2)
while res:
    print(res.val, end=' ')
    res = res.next