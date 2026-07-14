#Right pointer expands the window; left pointer shrinks it until the window becomes valid again.
class Solution(object):
        
    def lengthOfLongestSubstring(self, s):
        left = 0
        h = {}
        result = 0
        for right in range(len(s)):
        # Add current character
            h[s[right]]=h.get(s[right],0)+1
        # While window is invalid
            while h[s[right]]>1:
                h[s[left]]-=1
                left+=1
        
            result=max(right-left+1,result)
        return result
