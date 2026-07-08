import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low,high=1,max(nums)
        result=high
        divisor=1
        while low<=high:
            mid=(low+high)//2
            a=0
            for n in nums:
                a+=math.ceil(float(n)/mid)
            if a<=threshold:
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result


        
