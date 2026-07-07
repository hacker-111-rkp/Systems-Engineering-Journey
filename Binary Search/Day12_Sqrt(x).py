class Solution(object):
    def mySqrt(self, x):
        low,high=0,x
        result=0
        while low<=high:
            mid=(low+high)//2
            if mid**2 > x:
                high=mid-1
            elif mid**2 < x:
                low=mid+1
                result=mid
            else:
                return mid
        return result

    

        
