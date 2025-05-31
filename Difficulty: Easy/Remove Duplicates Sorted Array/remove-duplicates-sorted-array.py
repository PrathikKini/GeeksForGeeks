#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        idx = 0
        for i in range(len(arr)):
            if arr[idx] != arr[i]:
                idx+=1
                arr[idx] = arr[i]
        return idx + 1