class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(k):
            h={}
            left=0
            result=0
            for right in range(len(nums)):
                h[nums[right]]=h.get(nums[right],0)+1
                while len(h)>k:
                    h[nums[left]]-=1
                    if h[nums[left]]==0:
                        del h[nums[left]]
                    left+=1
                result+=(right-left+1)
            return result
        return atmost(k)-atmost(k-1)
        
