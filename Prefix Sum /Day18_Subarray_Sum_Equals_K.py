class Solution(object):
    def subarraySum(self, nums, k):
        # not using sliding window as this question can also contain negative numbers read constraints
        h={0:1}
        count=0
        #making nums as prefix sum 
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        #formula) current Prefix - previous prefix = k (targted sum )
        #rearrange it as ) previous prefix =current prefix -k
        for prefix in nums:
            count+=h.get(prefix-k,0)
            h[prefix]=h.get(prefix,0)+1
            
        return count

            
        
