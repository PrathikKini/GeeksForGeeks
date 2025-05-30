#User function Template for python3

class Solution:
    def dupLastIndex(self, arr):
        # Complete the function
        if len(arr) < 2:
            return [-1,-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == arr[i-1]:
                return [i,arr[i]]
        return [-1,-1]
    
