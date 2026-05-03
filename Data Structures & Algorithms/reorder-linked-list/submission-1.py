# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            curr = head
            prev =None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev=curr
                curr = nxt
            return prev
        head2 = slow.next
        slow.next=None
        curr2= reverse(head2)
        curr1 = head
        print(slow.val)
        while curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
        # return head1