#tc--o(n),sc--o(1)
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        left=0
        window=0# sum of disatisfied 
        satisfied=0 # sum of satisfaction 
        result=0
        for right in range(len(grumpy)) :
            if grumpy[right] : #True or 1 
                window+=customers[right]
            else:
                satisfied+=customers[right]
            if right-left+1>minutes:
                if grumpy[left]:#will be 1 then only remove 
                    window-=customers[left]
                left+=1
            result=max(result,window)
        return result+satisfied    
