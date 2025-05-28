#User function Template for python3

class Solution:
    def findIndex(self, arr, x):
        #code
        return max((i for i,n in enumerate(arr,1) if x == n), default=-1)