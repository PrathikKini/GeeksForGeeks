#User function Template for python3

class Solution:
    def countSquares(self, N):
        # code here 
        low, high = 1, N - 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid < N:
                low = mid + 1
            else:
                high = mid - 1
        return high



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends