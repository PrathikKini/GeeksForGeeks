#User function Template for python3

class Solution:
    def checkSquares(self, N):
        # code here 
        for a in range(int(math.sqrt(N))+1):
            b_squared = N - a*a
            b = int(math.sqrt(b_squared))
            if b*b == b_squared:
                return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.checkSquares(N))
# } Driver Code Ends