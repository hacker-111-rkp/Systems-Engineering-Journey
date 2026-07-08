import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low,high=1,max(piles)# low cant be 0 as it is min eating speed
        #in this low and high are not indices they are piles
        result=high
        while low<=high:
            a=0
            k=(low+high)//2
            for p in piles:
                a += math.ceil(float(p)/k) # ans to round of to its greater integer side 
            if a <= h:
                result = k
                high=k-1
            else:
                low=k+1
        return result
