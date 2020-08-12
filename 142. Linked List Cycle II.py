
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next: #当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            if head == slow:
                return head
            while head is not slow:
                head, slow = head.next, slow.next
            return head
    return None
    
 
 
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
    p9.next = p6
    print(detectCycle(head))
    