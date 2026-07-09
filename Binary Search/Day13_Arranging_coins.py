#brute force 
# this code will give memory exeed error because what if the number is 123213122211 this ? 
class Solution(object):
    def arrangeCoins(self, n):
        result=n
        store=0
        for i in range(1,n+1):
            result=result-i
            if result>=0:
                store = i           
        return store

#binary search 
class Solution(object):
    def arrangeCoins(self, n):
        low=1
        high=n
        result=1
        while low<=high:           
            mid=(low+high)//2
            sum1=(mid*(mid+1))//2
            if sum1>n:
                high=mid-1
            else:
                low=mid+1
                result=max(result,mid)
        return result    


        
        
