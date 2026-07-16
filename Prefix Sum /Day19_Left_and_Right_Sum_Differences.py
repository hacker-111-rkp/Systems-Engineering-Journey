
class Solution(object):
    def leftRightDifference(self, nums):
        left=0
        total=sum(nums)
        re=[]
        leftSum=[0]*len(nums)
        rightSum=[0]*len(nums)
        for i in range(len(nums)):
            right=total-nums[i]-left
            
            re.append(abs(right-left))
            left+=nums[i]
        return re 
             

        
        
