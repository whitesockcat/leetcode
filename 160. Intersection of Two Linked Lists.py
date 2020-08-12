
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1
        
 
if __name__=="__main__":
    head1 = ListNode(4)
    p1 = ListNode(1)
    p2 = ListNode(8)
    p3 = ListNode(4)
    p4 = ListNode(5)
    head2 = ListNode(5)
    a2 = ListNode(0)
    a3 = ListNode(1)
    
    head1.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = None
    head2.next = a2
    a2.next = a3
    a3.next = p2
    res = getIntersectionNode(head1,head2)
    while res:
        print(res.val, end=' ')
        res = res.next
    