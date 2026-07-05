#hashmap
#TC--O(n+m),SC--O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        h={}
        if len(magazine)<len(ransomNote):
            return False
        for i in magazine:
            h[i]=h.get(i,0)+1
        for j in ransomNote:
            if j not in h or h[j]==0:
                return  False
            h[j]-=1
        return True
sol=Solution()
print(sol.canConstruct("aa","aab"))
#Counter
#TC--O(n+m),SC--O(n)
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        a=Counter(magazine)
        for i in ransomNote:
            if i not in a or a[i]<=0:
                return False
            a[i]-=1
        return True
sol=Solution()
print(sol.canConstruct("aa","ab"))
#fixed array
#TC--O(n+m),SC--O(1)
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count=[0]*26
        for i in magazine:
            count[ord(i)-ord('a')]+=1
        for j in ransomNote :
            index= ord(j)-ord('a')
            if count[index]==0:
                return False
            count[index]-=1
        return True
sol=Solution()
print(sol.canConstruct("aa","ab"))
        

