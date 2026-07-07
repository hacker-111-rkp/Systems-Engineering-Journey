class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            #left sorted array
            if nums[low]<=nums[mid]:
                if  target<nums[low] or nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            # right sorted array 
            if nums[high]>=nums[mid]:
                if target < nums[mid] or target> nums[high]:
                    high=mid-1
                else:
                    low=mid+1
 
        return -1
                

                    
        
