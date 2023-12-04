#User function Template for python3

class Solution:
    def numOfPerfectSquares(self, a, b):
        # code here
        start = int(a**0.5)
        end = int(b**0.5)
        cnt = end - start + (1 if start**2>=a else 0)
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(int,input().split())
        
        ob = Solution()
        print(ob.numOfPerfectSquares(a,b))
# } Driver Code Ends