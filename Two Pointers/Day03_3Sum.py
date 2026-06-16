#this code sc is not good 
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result=set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[left]+nums[right]+nums[i]
                if sum==0:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    right-=1
        return [list(x) for x in result]
sol=Solution()
print(sol.threeSum([-1,0,1,2,-2,-4]))
#better sc o(1) code 
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
        
