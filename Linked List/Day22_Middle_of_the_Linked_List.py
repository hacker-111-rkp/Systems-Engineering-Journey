class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:        
         
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        mid=len(nodes)//2
        return nodes[mid]
#or 
'''

def middleList(head):
    slow,fast=head,head
    while fast and  fast.next :
        slow=slow.next
        fast=fast.next.next
    return slow
    

'''
        

