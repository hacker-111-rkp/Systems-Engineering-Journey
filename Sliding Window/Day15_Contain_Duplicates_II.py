class Solution(object):
    '''def containsNearbyDuplicate(self, nums, k):
        window=set()
        for index,value in enumerate(nums):
            if value in window:
                return True 
            window.add(value)
            if len(window)>k:
                window.remove(nums[index-k])
        return False
sol=Solution()
print(sol.containsNearbyDuplicate([5,2,3,1,3,3],3))'''

#sliding window
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):  
        window =set()
        for i,j in enumerate(nums):
            if j in window:
                return True
            window.add(j)
            if len(window)>k:
                window.remove(nums[i-k])
        return False

