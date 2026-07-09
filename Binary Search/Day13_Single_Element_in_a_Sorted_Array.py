#core logic-- after cancelling the mid like if it contain a duplicate then see which other sides contain odd values --my method with index separating of odd and even observation 
class Solution(object):
    def singleNonDuplicate(self, nums):
        low=0
        high=len(nums)-1
        mid=(low)
        
        while low<=high:
            mid=(low+high)//2
            if len(nums)==1 or mid==0 or mid==len(nums)-1:
                return nums[mid]
            elif nums[mid]==nums[mid-1] and mid>0:
                if mid%2==0:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]==nums[mid+1] and mid<len(nums)-1:
                if mid%2==0:
                    low=mid+1
                else:
                    high=mid-1
            else:
                return nums[mid]
        return nums[mid]        
