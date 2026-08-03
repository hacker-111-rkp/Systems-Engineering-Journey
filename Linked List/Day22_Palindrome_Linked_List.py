
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        curr=head
        values=[]
        while curr:
            values.append(curr.val)
            curr=curr.next
        return values[::-1]==values
    

            
