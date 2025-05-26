#User function Template for python3

class Solution:
    def altProduct(self, arr):
       # Your code goes here
       n = len(arr)
       arr.sort()
       total = 0
       for i in range(n//2):
           total += arr[i] * arr[n-i-1]
       return total