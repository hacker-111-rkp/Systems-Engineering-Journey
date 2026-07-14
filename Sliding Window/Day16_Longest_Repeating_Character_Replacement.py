
class Solution(object):
    def characterReplacement(self, s, k):
        left=0
        h={}
        count=0
        result=0
        for right in range(len(s)):
            h[s[right]]=h.get(s[right],0)+1
            count=max(count,h[s[right]])
            #window_size=right-left+1, here count is max_frequency            
            
            while (right-left+1)-count>k:
                h[s[left]]-=1
                if h[s[left]]==0:
                    del h[s[left]]
                left+=1
            result=max(result,right-left+1)
        return result
        
