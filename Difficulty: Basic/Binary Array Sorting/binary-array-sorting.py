
class Solution:
    # Function to sort the binary array in non-decreasing order
    def binSort(self, arr):
        # code here
        l , r = 0 , len(arr) - 1
        while l <= r:
            if arr[l] == 0: 
                l += 1
            else:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
        return arr

