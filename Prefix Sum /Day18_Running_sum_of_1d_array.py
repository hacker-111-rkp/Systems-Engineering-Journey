'''
class Solution(object):
    def runningSum(self, nums):
        sum=0
        opp=[]
        for i in nums:
            sum+=i
            opp.append(sum)
        return opp
        
sol=Solution()
print(sol.runningSum([1,1,1,1,1]))
'''
#resolved by prefix sum 
class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
