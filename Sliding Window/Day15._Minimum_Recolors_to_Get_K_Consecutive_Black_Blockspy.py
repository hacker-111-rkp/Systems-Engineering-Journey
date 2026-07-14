class Solution(object):
    def minimumRecolors(self, blocks, k):
        count=0
        left=0
        h={}
        count=len(blocks)
        # for 1st window
        for right in range(k):
            h[blocks[right]]=h.get(blocks[right],0)+1
        count=min(count,h.get('W',0))
        for right in range(k,len(blocks)):
            h[blocks[right]]=h.get(blocks[right],0)+1
            if right-left+1>k:
                h[blocks[left]]-=1
                if h[blocks[left]]==0:
                    del h[blocks[left]]
                left+=1
            count=min(count,h.get('W',0))
        return count
    
            
            


        
