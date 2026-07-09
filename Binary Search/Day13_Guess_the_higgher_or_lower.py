
class Solution(object):
    def guessNumber(self, n):# n--uppper bound   
        low=1
        high=n

        while low<=high:
            mid=(low+high)//2
            result=guess(mid)# this will retuen all 3 case 
            if result==1:#or >0
                low=mid+1
            elif result== -1:# or <0
                high=mid-1
            else: # ==0
                return mid


        
