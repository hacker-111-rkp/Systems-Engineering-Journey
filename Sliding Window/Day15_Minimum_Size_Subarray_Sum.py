class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        window=0
        result=float('inf')
        for right in range(len(nums)):            
            window+=nums[right]
            while window>=target:
                result=min(result,right-left+1)
                window-=nums[left]
                left+=1
                
        if result == float('inf'):
            return 0
        else:
            return result 

         
        
