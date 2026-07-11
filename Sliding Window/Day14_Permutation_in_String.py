
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        k=len(s1)
        h1={}
        h2={}
        #frequency of s1
        for j in s1:
            h2[j]=h2.get(j,0)+1
        #frequency of s2 first window
        for x in s2[:k]:A
            h1[x] = h1.get(x,0)+1
        if h1==h2:
            return True
        for i in range(k,len(s2)):
            h1[s2[i]] = h1.get(s2[i],0)+1
            h1[s2[i-k]] -= 1
            if h1[s2[i-k]] == 0:
                del h1[s2[i-k]]
            if h1==h2:
                return True
        return False
