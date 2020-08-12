#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 虽然只写了一个循环 但是可能因为如果k很大 我这个还是要遍历两次链表 所以时间差不多
        # slow = ListNode(None)
        # fast = ListNode(None)
        # slow.next = head
        # fast.next = head
        # h = tail = head
        # K = k
        # Flag = False
        # if not head:
        #     return None
        # elif not head.next:
        #     return head
        # if not k:
        #     return head
        # while tail:
        #     if k == 0:
        #         slow.next = head
        #         slow = head
        #         head = head.next
        #     else:
        #         k -= 1
        #     if not Flag:
        #         fast = fast.next
        #     tail = tail.next
        #     # print(k)
        #     if not tail:
        #         if k >0:
        #             l = K - k
        #             k = K % l
        #             tail = h
        #             Flag = True
        #             # fast.next = tail
        # top = slow.next if slow.next else h
        # if top != h:
        #     fast.next = h
        # slow.next = None
        # return top
        
        #==================================
        # if not head:return head
        # # 获取链表长度
        # l = 0
        # node = head
        # while node:
        #     l+=1
        #     node = node.next
        # k = k % l # 取余，避免重复循环
        # if k == 0:
        #     return head
        # pre,post = head,head    # 定义双指针
        # for i in range(k):
        #     post = post.next    # 后指针先走K步
        # while post.next:        # 一起走，直到后指针走到链表尾端
        #     pre = pre.next
        #     post = post.next

        # tmp = pre.next          # 记录头结点
        # pre.next = None         # 将链表截断
        # post.next = head        # 将链表翻转连接
        # return tmp
        
        #==================================
        if not head:return head
        num=1
        ptr=head
        while ptr.next:
            ptr=ptr.next
            num+=1
        ptr.next=head
        count=num-k%num
        while count>0:
            ptr=head
            head=head.next
            count-=1
        ptr.next=None
        return head



mm = Solution()
head = ListNode(None)
cur = head
for i in [1,2,3,4,5]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next

res = mm.rotateRight(head, 10)
while res:
    print(res.val, end=' ')
    res = res.next

# @lc code=end

