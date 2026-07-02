#brute force 
#tc--o(nlogn) , sc--o(1)
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
            
sol=Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
#two pointers 
#tc--o(n) , sc--o(n)
class Solution(object):
    def sortedSquares(self, nums):
        left=0
        n=len(nums)
        right =n-1
        index=n-1
        ans=[0]*n
        while left<= right :
            if abs(nums[left])<abs(nums[right]):
                ans[index]=nums[right]**2
                right-=1
            else:
                ans[index]=nums[left]**2
                left+=1
            index-=1
        return ans
            
sol=Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
