#User function Template for python3
class Solution:
    def squaresDiff (self, N):
        # code here 
        a = sum([i**2 for i in range(1,N+1)])
        b = sum([i for i in range(1,N+1)])**2
        return abs(a-b)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.squaresDiff(N))
# } Driver Code Ends