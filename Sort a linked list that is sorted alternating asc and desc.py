class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
要求将一个奇数位升序，偶数位降序的链表转成一个升序的链表。
Input List:   10->40->53->30->67->12->89->NULL
Output List:  10->12->30->40->53->67->89->NULL
'''
class Solution:
    def reverse(self, head):
        p = None
        while head:
            t = head.next
            head.next = p
            p = head
            head = t
        return p
    def split_odd_even(self, head):
        odd = odd_s = head
        even = even_s = head.next
        if not even:
            odd.next = None
            return odd, even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        if odd:
            odd.next = None
        if even:
            even.next = None
        return odd_s, even_s
    def sortAndConcatTwoChain(self, l1, l2):
        dummy = ListNode(None)
        dummy.next = l1 if l1.val < l2.val else l2
        p = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        while p1:
            p.next = p1
            p = p.next
            if p1.next:
                p1 = p1.next
            else:
                p.next = None
                break
        while p2:
            p.next, p = p2, p.next
            if p2.next:
                p2 = p2.next
            else:
                p.next = None
                break
        return dummy.next
    def sortOddEvenBlaBla(self, head: ListNode) -> ListNode:
        # split odd even
        if not head:
            return head
        else:
            odd, even = self.split_odd_even(head)
            even = self.reverse(even)
            # print('odd', odd.val)
            # print('even', even.val)
            return self.sortAndConcatTwoChain(odd, even)




mm = Solution()
head = ListNode(None)
cur = head
for i in [10,40,53,30,67,12,89]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

res = mm.sortOddEvenBlaBla(head)
while res:
    print(res.val, end=' ')
    res = res.next