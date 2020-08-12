
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    p = None
    while head:
        t = head.next
        head.next = p
        p = head
        head = t
    return p
 
 
if __name__=="__main__":
    head = ListNode(-1)
    p1 = ListNode(-7)
    p2 = ListNode(7)
    p3 = ListNode(-4)
    p4 = ListNode(19)
    p5 = ListNode(6)
    p6 = ListNode(-9)
    p7 = ListNode(-5)
    p8 = ListNode(-2)
    p9 = ListNode(-5)
    head.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7
    p7.next = p8
    p8.next = p9
    p9.next = None
    res = reverseList(head)
    while res:
        print(res.val, end=' ')
        res = res.next
    