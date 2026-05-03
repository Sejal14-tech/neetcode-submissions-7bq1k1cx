# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = dummy
        slow = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast=fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        










        # def reverse(head):
        #     curr = head
        #     prev =None
        #     while curr:
        #         nxt = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = nxt
        #     return prev
        # rev = reverse(head)
        # if n == 1:
        #     rev = rev.next
        # else:
        #     curr = rev
        #     for _ in range(n - 2):
        #         curr = curr.next
        #     curr.next = curr.next.next

        # return reverse(rev)