#sorting 
#TC--O(nlog(n)), SC--O(n)# as sorting created a extra list n 
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t):
#hashmap
#TC--O(n),SC---O(n)
class Solution(object):
    def isAnagram(self, s, t):
        h={}
        if len(s)!=len(t):
            return False
        for i in s:
            h[i]=h.get(i,0)+1
        for i in t:
            if i not in h :
                return False
            h[i] -= 1
            if h[i]<0:
                return False
        return True
                
#two hashmap
#TC--O(n),SC---O(n)
class Solution(object):
    def isAnagram(self, s, t):
        h={}
        o={}
        #as dictionaries dont have to have same sequencee of keys to be equal
        for i in s:
            h[i]=h.get(i,0)+1
        for j in t:
            o[j]=o.get(j,0)+1
        return o==t

#counter
#TC--O(n),SC---O(n)
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)
#fixed array(very imp)
#TC--O(n),SC---O(1)
class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        for value in count:
            if value != 0:
                return False

        return True
        
