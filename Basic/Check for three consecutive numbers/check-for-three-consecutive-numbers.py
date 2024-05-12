#User function Template for python3
class Solution:
    def consecutiveSum (self, n):
        # code here 
        if n%3 == 0:
            return [n //3-1, n//3,n//3 +1]
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        list = ob.consecutiveSum(n)
        print(*list)
# } Driver Code Ends