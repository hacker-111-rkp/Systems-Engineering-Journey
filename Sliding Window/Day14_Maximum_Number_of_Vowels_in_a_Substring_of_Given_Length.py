class Solution(object):
    def maxVowels(self, s, k):
        vowels={'a','e','i','o','u'}
        count=0
        for i in s[:k]:
            if i in vowels :
                count+=1
        result=count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            result=max(result,count)
        return result


        


