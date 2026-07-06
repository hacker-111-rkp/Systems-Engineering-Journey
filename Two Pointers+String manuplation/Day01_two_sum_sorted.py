#brute force 
class Solution:
    def twoSum(self, numbers,target):
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1] # Return the indices (1-indexed)
                    # so index starting from 1 not 0
        return False
sol=Solution()
print(sol.twoSum([2,4,1,4],3))
# two pointers 
