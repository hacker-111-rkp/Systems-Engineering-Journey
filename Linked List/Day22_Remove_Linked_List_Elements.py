
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        while head and head.val == val:
            head=head.next
        curr=head
        while curr and curr.next:
            if curr.next.val!=val:
                curr=curr.next
            else:
                curr.next=curr.next.next
        return head

        
