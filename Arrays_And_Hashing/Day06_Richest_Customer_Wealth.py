
class Solution(object):
    def maximumWealth(self, accounts):
        digit=0
        for i in accounts:
            sum=0
            for j in i :
                sum+=j
            if digit < sum :
                digit=sum
        return digit
        
sol=Solution()
print(sol.maximumWealth([[3,2,1],[4,5,3]]))
#12
