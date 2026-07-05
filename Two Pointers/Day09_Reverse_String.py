
#two pointers 
#TC--O(n),SC--O(1)
class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
sol=Solution()
print(sol.reverseString(["h","e","l","l","o"]))

#slicing without creating a extra space 
#TC--O(1),SC--O(n)
class Solution(object):
    def reverseString(self, s):
        s[:]=s[::-1]
        return s
sol=Solution()
print(sol.reverseString(["h","e","l","l","o"]))
#build in function of reverse
#TC--O(n),SC--O(1)
class Solution(object):
    def reverseString(self, s):
        return s.reverse()
sol=Solution()
print(sol.reverseString(["h","e","l","l","o"]))
