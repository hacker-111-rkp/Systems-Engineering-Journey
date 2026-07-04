#hashmap
#tc--O(n), sc--O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for ind,key in enumerate(nums): # val --> index , key--> value/item
            if key in d:
                i,j=d[key],ind
                if abs(i-j)<=k:
                    return True 
            d[key]=ind
        else:
            return False
sol=Solution()
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))
#Sliding Window + HashSet

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window=set()
        for index,value in enumerate(nums):
            if value in window:
                return True 
            window.add(value)
            if len(window)>k:
                window.remove(nums[index-k])
        return False
sol=Solution()
print(sol.containsNearbyDuplicate([5,2,3,1,3,3],3))
#tc--O(N),SC--O(N)
