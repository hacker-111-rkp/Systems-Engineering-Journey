class Solution(object):
    def longestOnes(self, nums, k):
        h={}
        result=0
        left=0
        for right in range(len(nums)):        
            h[nums[right]]=h.get(nums[right],0)+1
                        
            while h.get(0,0)>k:
                result=max(result,right-left)
                h[nums[left]]-=1
                if h[nums[left]]==0:
                    del h[nums[left]]
                left+=1
            result = max(result, right - left + 1)
        return result
