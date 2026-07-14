#question is saying for longest subarray with 2 distinct trees or for only 2 typesof number
class Solution(object):
    def totalFruit(self, fruits):
        left=0
        window=0
        h={}
        result=0
        for right in range(len(fruits)):
            
            h[fruits[right]]=h.get(fruits[right],0)+1
            
            while len(h)>2:
                h[fruits[left]]-=1
                if h[fruits[left]]==0:
                    del h[fruits[left]]
                left+=1
            result=max(result,right-left+1)
        return result
