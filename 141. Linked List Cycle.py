
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def exitLoop(LList):
    p1 = p2 = LList
    while p2 and p2.next: #当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False
 
 
if __name__=="__main__":
    LList = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)
    p5 = ListNode(6)
    LList.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p2
    print(exitLoop(LList))
    