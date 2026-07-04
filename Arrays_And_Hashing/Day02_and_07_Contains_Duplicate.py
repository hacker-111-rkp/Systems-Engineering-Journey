
#extra dict 
class Solution(object):
    def containsDuplicate(self, nums):
        hash={}
        for i in nums:
            if i in hash:
                return True
                break
            hash[i]=1
        else:
            return False
sol=Solution()
print(sol.containsDuplicate([1,2,2,3,4]))
#hash set 
class Solution:
    def hasDuplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))
#one liner set
class Solution:
    def hasDuplicate(self, nums):
        a=set(nums)
        if len(a)==len(nums):
            return False
        return True
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))
#sorting 
class Solution:
    def hasDuplicate(self,nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))
#brute force will give TLE
