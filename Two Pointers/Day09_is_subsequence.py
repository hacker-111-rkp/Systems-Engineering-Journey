#two pointers
#tc--o(n),sc--o(1)
class Solution(object):
    def isSubsequence(self, s, t):
        l,r=0,0
        while l<len(s) and r<len(t):
            if len(s)>len(t):
                return False
            if s[l]==t[r]:
                l+=1
            r+=1
        return l==len(s)
