# this will change the exising nums list
class Solution(object):
    def getConcatenation(self, nums):
        nums.extend(nums)
        return nums 
sol=Solution()
print(sol.getConcatenation([1,2,3,4]))

# much good 
class Solution(object):
    def getConcatenation(self, nums):
        return nums+nums
sol=Solution()
print(sol.getConcatenation([1,2,3,4]))
