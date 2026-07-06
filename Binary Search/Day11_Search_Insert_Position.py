
#TC--O(logn),SC--O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        return low

                       
sol=Solution()
print(sol.searchInsert([1,3,5,7,9],7))
        
