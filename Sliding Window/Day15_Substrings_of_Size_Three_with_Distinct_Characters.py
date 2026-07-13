class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        window={}
        k=3
        left=0
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            if right-left+1>k:
                window[s[left]]-=1
                if  window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if right - left + 1 == k:
                if len(window) == k:
                    count += 1                   
        return count    
            

        
