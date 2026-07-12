
class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            #for duplicates
            if nums[mid]==nums[low]==nums[high]:
                low+=1
                high-=1
                continue
            #left sorted array
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            # right sorted array 
            else:#ofc if left is not sorted then right will be
                if nums[high]>=target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
 
        return False
                

                    
                
        
