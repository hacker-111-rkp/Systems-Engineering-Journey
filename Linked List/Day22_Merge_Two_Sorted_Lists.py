

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        curr=dummy
        while list1 is not None and list2 is not None:
            if list1.val>list2.val:
                curr.next=list2
                list2=list2.next
            else: 
                curr.next=list1
                list1=list1.next
            curr=curr.next
        if list1 is not None:
            curr.next=list1
            curr=curr.next
        if list2 is not None:
            curr.next=list2
            curr=curr.next
        return dummy.next
        
        
        
        
        
