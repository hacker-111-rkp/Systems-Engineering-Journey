class Solution(object):
    def longestSubarray(self, nums):
        h={}
        result=0
        left=0
        for right in range(len(nums)):
            h[nums[right]]=h.get(nums[right],0)+1
                
            while h.get(0,0)>1:
                h[nums[left]]-=1
                if h[nums[left]]==0:
                    del h[nums[left]]
                left+=1
            result=max(result,right-left)# as we have to delete 0
        return result
        
        
