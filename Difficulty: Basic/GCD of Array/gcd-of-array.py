#User function Template for python3
class Solution:   
    def gcd_find(self, a, b):
        # code here 
        while b!= 0:
            a, b = b, a % b
        return a
        
    def gcd(self,n,arr):
        result = arr[0]
        for i in range(1,len(arr)):
            result = self.gcd_find(result,arr[i])
        return result