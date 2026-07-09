class Solution(object):# in this ships == no of days 
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high =sum(weights)
        result =high
        def function(mid):
            ships,capacity=1,mid
            for w in weights:
                if capacity -w<0:
                    ships+=1
                    capacity=mid
                capacity -=w
            return  ships<=days
        while low<=high:
            mid=(low+high)//2
            if function(mid):
                result=min(mid,result)
                high=mid-1
            else:
                low=mid+1
        return result
            
                
        
