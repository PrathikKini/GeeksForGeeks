#User function Template for python3

class Solution:
    def strangeSort (self,arr, k):
        # your code here
        res = arr[k-1]
        del arr[k-1]
        arr.sort()
        arr.insert(k-1,res)