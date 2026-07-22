class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:        
         
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        mid=len(nodes)//2
        return nodes[mid]
        


