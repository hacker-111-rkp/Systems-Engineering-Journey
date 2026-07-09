class Solution(object):
    def firstBadVersion(self, n):
        low=1
        high=n
        result1=high
        while low<=high:
            mid=(low+high)//2
            result=isBadVersion(mid)
            if result is True:
                high=mid-1
                result1=min(mid,result1)
            else:
                low=mid+1
        return result1
        
