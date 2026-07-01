#tc--o(n)
#sc -- o(n)
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

# more optimal as sc =o(1)
def runningSum(nums):
    # Start from index 1, adding the previous element's value to the current one
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
