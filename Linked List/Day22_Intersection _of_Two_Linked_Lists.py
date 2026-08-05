
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#note you cant relink the nodes values only the nodes can relink 
class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None
        curr=head
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while curr and curr.next:
            temp=curr.next
            new=temp.next
            temp.next=curr
            prev.next=temp
            curr.next=new
            prev=curr
            curr=curr.next
            
        return dummy.next

        
