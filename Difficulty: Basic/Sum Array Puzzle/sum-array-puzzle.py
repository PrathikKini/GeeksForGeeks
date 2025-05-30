class Solution:
    def sumArray(self, arr):
        s = sum(arr)
        for i in range(len(arr)):
            arr[i]=s-arr[i]
        return arr
        