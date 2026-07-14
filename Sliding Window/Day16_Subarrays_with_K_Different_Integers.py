#note the pattern of this atmost 
'''Ask yourself:
Can I easily count "at most K", but the question wants "exactly K"?

After I make my window valid, how many valid subarrays end at right?
Count of valid subarrays--->result += (right - left + 1)
'''
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(k):
            h={}
            left=0
            result=0
            for right in range(len(nums)):
                h[nums[right]]=h.get(nums[right],0)+1
                while len(h)>k:
                    h[nums[left]]-=1
                    if h[nums[left]]==0:
                        del h[nums[left]]
                    left+=1
                result+=(right-left+1)# gives all the subarray sum 
            return result
        return atmost(k)-atmost(k-1)
        
