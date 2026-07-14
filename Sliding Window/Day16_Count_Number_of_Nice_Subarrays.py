
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atmost(k):
            count=0
            left=0
            window=0
            result=0
            for right in range(len(nums)):
                if nums[right]%2!=0:
                    count+=1
                while count>k:                   
                    window-=nums[left]
                    if nums[left] % 2 != 0:
                        count -= 1
                    left+=1
                result+=(right-left+1)
            return result
        return atmost(k)-atmost(k-1)
                
        return result
        
