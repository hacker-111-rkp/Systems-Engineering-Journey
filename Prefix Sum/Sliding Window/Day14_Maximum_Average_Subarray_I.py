class Solution(object):
    def findMaxAverage(self, nums, k):
        sum1=sum(nums[:k])
        result=float(sum1)/k # used float as int/int is always int 
        for i in range(k,len(nums)):
            sum1+=nums[i]-nums[i-k]
            average=float(sum1)/k
            result=max(result,average)
        return result


        
        
        
