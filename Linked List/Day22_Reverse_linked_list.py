# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         # val: current node value
#         # next: pointer to the next node
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers
        prev = None
        curr = head
        
        # Traverse through the list
        while curr:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the link
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        # prev will be pointing to the new head of the reversed list
        return prev

