class Solution(object):
    def isPerfectSquare(self, num):
        low,high=0,num
        result=0
        while low<=high:
            mid=(low+high)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                result=mid
                high=mid-1
                if mid**2<num:
                    return False
            else:
                low=mid+1
        return False

            

    

        
        
