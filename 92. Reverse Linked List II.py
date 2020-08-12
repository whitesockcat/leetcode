
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head: ListNode, m, n) -> ListNode:
    dummy = p = ListNode(None)
    dummy.next = head
    p.next = head
    for i in range(m-1):
        p = p.next
    one = p
    two = head = p.next
    for i in range(m, n+1):
        t = head.next
        head.next = p
        p = head
        if i != n:
            head = t
        
    one.next = head
    two.next = t
    return dummy.next
        
 
if __name__=="__main__":
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)
    head.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = None
    res = reverseBetween(head,2,4)
    while res:
        print(res.val, end=' ')
        res = res.next
    