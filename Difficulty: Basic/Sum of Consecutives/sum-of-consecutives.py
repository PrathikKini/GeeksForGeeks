#User function Template for python3
class Solution:
    def canBeSumofConsec (self, n):
        # code here 
        return "0" if (n & (n-1)) == 0 else "1"