#hash map
class Solution:
    def hasDuplicate(self,nums):
        count=0
        hashmap={}
        for i,number in enumerate(nums):
            if number in hashmap:
                return True
            else :
                hashmap[number]=i
        return False
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))
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
