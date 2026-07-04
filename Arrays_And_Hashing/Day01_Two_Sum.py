#hash map method 
class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for index,value in enumerate(nums):
            num = target - value
            if num in hashmap:
                return index,hashmap[num]
            hashmap[value]=index

sol=Solution()
print(sol.twoSum([2,7,11,15],9))
        

#brute force 
class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return False
sol = Solution()
a=sol.twoSum([3,4,5,6],7)
print(a)
#two pointers 
class Solution:
    def twoSum(self,nums,target):
        nums.sort()
        left = 0
        right = len(nums)-1
        while left<right :
            sum= nums[left]+nums[right]
            if sum<target:
                left+=1
            elif sum == target:
                return [left , right ]
            else:
                right-=1 
sol = Solution()
a=sol.twoSum([3,4,5,6],7)
print(a)
