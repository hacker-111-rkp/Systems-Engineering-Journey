#tc--O(n),sc--o(n)
class Solution(object):  
    def moveZeroes(self, nums):
        arr=[]
        zero_count=0
        n=len(nums)-1
        for i in nums:
            if i!=0:
                arr.append(i)
            else:
                zero_count+=1
        
        arr.extend([0]*zero_count) 
        nums[:]=arr
        return nums
        

sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))
#two pointers method (over writes )
#tc--o(n) , sc --o(1)
class Solution(object):
    def moveZeroes(self, nums):
        left=0
        for right in range(len(nums)):
            if nums[right] !=0:
                nums[left]=nums[right]
                left+=1
        while left<len(nums):
            nums[left]=0
            left+=1
        return nums
sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))

# two pointer (swap method)
#tc--o(n) , sc --o(1)
class Solution(object):
    def moveZeroes(self, nums):
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums
sol=Solution()
print(sol.moveZeroes([1,0,7,3,12]))



