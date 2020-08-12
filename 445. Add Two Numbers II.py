class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head):
        p = None
        while head:
            t = head.next
            head.next = p
            p = head
            head = t
        return p
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10 
            l1 = l1.next if l1 else None           
            l2 = l2.next if l2 else None
        return self.reverse(dummy.next)

mm = Solution()
head = ListNode(None)
cur = head
for i in [7,2,4,3]:
    cur.next = ListNode(i)
    cur = cur.next
head1 = head.next
head = ListNode(None)
cur = head
for i in [5,6,4]:
    cur.next = ListNode(i)
    cur = cur.next
head2 = head.next

# res = mm.reverse(head2)
# while res:
#     print(res.val, end=' ')
#     res = res.next
res = mm.addTwoNumbers(head1, head2)
while res:
    print(res.val, end=' ')
    res = res.next