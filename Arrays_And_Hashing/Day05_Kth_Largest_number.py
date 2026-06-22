#SOLVED BY SORTING
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]
sol=Solution()
print(sol.findKthLargest([3,2,1,5,6],2)
