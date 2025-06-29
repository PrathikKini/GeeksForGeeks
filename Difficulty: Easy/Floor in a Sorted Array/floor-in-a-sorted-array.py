class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        l = 0
        h = len(arr) - 1
        floor_idx = -1
        
        while l<=h:
            m = (l+h) // 2
            if arr[m] == x:
                floor_idx = m
                l = m + 1
            elif arr[m] < x:
                floor_idx = m
                l = m + 1
            else:
                h = m - 1
        return floor_idx
        