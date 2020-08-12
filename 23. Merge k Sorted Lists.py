from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge_both(self, l1: ListNode, l2: ListNode):
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        # else:
        #     tmp = lists[0]
        #     for i in range(1,n):
        #         tmp = self.merge_both(tmp, lists[i])
        # return tmp
        else:
            pairs = lists
            while len(pairs) > 1:
                n = len(pairs)
                if n & 1 == 1:
                    pairs.append(None)
                pairs = [self.merge_both(pairs[i*2], pairs[i*2+1])
                        for i in range(((n+1)//2))]
        return pairs[0] if pairs else None
        

mm = Solution()
head = ListNode(None)
cur = head
for i in [1,4,5]:
    cur.next = ListNode(i)
    cur = cur.next
head1 = head.next
head = ListNode(None)
cur = head
for i in [1,3,4]:
    cur.next = ListNode(i)
    cur = cur.next
head2 = head.next
head = ListNode(None)
cur = head
for i in [2,6]:
    cur.next = ListNode(i)
    cur = cur.next
head3 = head.next

res = mm.mergeKLists([head1, head2, head3])
while res:
    print(res.val, end=' ')
    res = res.next