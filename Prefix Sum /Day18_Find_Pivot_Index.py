class Solution(object):
    def pivotIndex(self, nums):  
     #brute force    
        for i in range(len(nums)):
            right_sum=0
            left_sum=0
            if i==len(nums)-1:
                right_sum=0
            else:
                right_sum=sum(nums[i+1:])
            if i==0:
                left_sum=0
            else:
                left_sum=sum(nums[:i])
            if right_sum==left_sum:
                return i
        return -1
 # prefix sum 
class Solution(object):
    def findMiddleIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1



        
