#User function Template for python3

class Solution:
    def bitMultiply(self, N):
        # code here
        res = bin(N)[2:].count('1')
        return N*res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.bitMultiply(N))

# } Driver Code Ends