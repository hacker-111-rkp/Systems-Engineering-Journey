# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        #reversing the second list 
        prev=None
        curr=second
        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        first=head
        second=prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
        return head
    
            
            
            
        
            


        
