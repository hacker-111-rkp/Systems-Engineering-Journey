class Solution(object):
    def pivotIndex(self, nums):  
        
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
                



        
