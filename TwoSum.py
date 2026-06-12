#hash map method 
class Solution:
    def twoSum(self,nums,target):
        hashmap={}
        for i,nums in enumerate(nums):
            complement = target - nums   
            if complement in hashmap:
                return [hashmap[complement] , i ]
            
            hashmap[nums] = i

sol = Solution()
a=sol.twoSum([3,4,5,6],7)
print(a)

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
def two_sum_two_pointers(nums: list[int], target: int) -> list[int]:

    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right] 
            
        
        elif current_sum < target:
            left += 1
            
        
        else:
            right -= 1
            
    return [] 
