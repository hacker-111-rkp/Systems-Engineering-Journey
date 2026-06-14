#brut force 
class Solution:
    def isPalindrome(self,s):
        empty=""
        for i in s : 
            if i.isalnum():# isalnum accepts  number and  alphabets 
                empty+=i.lower()
        return empty[::]==empty[::-1]
sol=Solution()
print(sol.isPalindrome("hello"))
print(sol.isPalindrome("Was it a car or a cat I saw?"))
# two pointers 
class Solution:
    def isPalindrome(self,s):
        
        l, r = 0, len(s)-1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
sol=Solution()
print(sol.isPalindrome("hello"))
print(sol.isPalindrome("Was it a car or a cat I saw?"))
#stack method 
class Solution:
    def isPalindrome(self,s):
        
        cleaned = []

        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())

        stack = cleaned[:]

        for ch in cleaned:
            if ch != stack.pop():
                return False

        return True
sol=Solution()
print(sol.isPalindrome("hello"))
print(sol.isPalindrome("Was it a car or a cat I saw?"))
        

    
