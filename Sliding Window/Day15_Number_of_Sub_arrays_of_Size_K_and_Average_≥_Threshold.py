class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        left=0
        window=0
        count=0
        #for 1st window
        for right in range(k):
            window+=arr[right]
        average=window//k
        if average>=threshold:
            count+=1
        #for remaining window
        for right in range(k,len(arr)):
            window+=arr[right]
            if right-left+1 >k:
                window-=arr[left]
                left+=1
            average=window//k
            if average>=threshold:
                count+=1
        return count

        
