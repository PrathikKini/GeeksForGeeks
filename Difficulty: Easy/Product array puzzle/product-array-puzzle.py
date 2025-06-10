#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        prefix = postfix = 1
        res = [1] * len(arr)
        for i in range(len(arr)):
            res[i] = prefix
            prefix *= arr[i]
        for i in range(len(arr)-1,-1,-1):
            res[i] *= postfix
            postfix *= arr[i]
        
        return res