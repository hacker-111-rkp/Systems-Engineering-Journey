class Solution(object):
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        k=len(p)
        h1={}
        h2={}
        re=[]
        # for p in h2 frequency
        for j in p[:]:
            h2[j]=h2.get(j,0)+1
        # for 1st window in h1
        for j in s[:k]:
            h1[j]=h1.get(j,0)+1
        if h1==h2:
            re.append(0)
        # all windows frequency
        for i in range(k,len(s)):
            h1[s[i]]=h1.get(s[i],0)+1
            h1[s[i-k]]-=1
            if h1[s[i-k]] == 0:
                del h1[s[i-k]]
            if h1==h2:
                re.append(i-k+1)
        return re

