class Solution:
    def findExtra(self,a,b):
        #add code here
        low = 0
        high = len(b) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if a[mid] == b[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low