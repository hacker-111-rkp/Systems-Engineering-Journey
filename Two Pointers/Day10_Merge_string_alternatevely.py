#two pointers 
#TC--O(N+M), SC--O(N+M)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        left,right=0,0
        h=[]
        while left<len(word1) and right<len(word2):
            h.append(word1[left])
            h.append(word2[right])
            right+=1
            left+=1
        while left<len(word1):
            h.append(word1[left])
            left+=1
        while right<len(word2):
            h.append(word2[right])
            right+=1
        return "".join(h)
#ZIP METHOD
#TC--O(N+M), SC--O(N+M)
from itertools import zip_longest
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = []
        for a, b in zip_longest(word1, word2, fillvalue=""):
            ans.append(a)
            ans.append(b)

        return "".join(ans)
#single loop
#TC--O(N+M), SC--O(N+M)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans.append(word1[i])

            if i < len(word2):
                ans.append(word2[i])

        return "".join(ans)
