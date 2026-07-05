#hashmap
#TC--O(n),SC--O(n)
class Solution(object):
    def firstUniqChar(self, s):
        h={}
        for i in  s:
            h[i]=h.get(i,0)+1
        for index,value in enumerate(s):
            if h[value]==1:
                return index
                break
        return -1
#counter
#TC--O(n),SC--O(n)
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        a=Counter(s)
        for i,j in enumerate(s) :
            if a[j]==1:
                return i
        return -1
#frequency array(26 letter) or fixed array
#TC--O(n),SC--O(1)
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        count=[0]*26
        for i in s :
            count[ord(i)-ord('a')]+=1
        for j,k in enumerate(s):
            if count[ord(k)-ord('a')]==1:
                return j
        return -1

        
