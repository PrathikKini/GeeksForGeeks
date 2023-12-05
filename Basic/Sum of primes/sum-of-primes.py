#User function Template for python3

class Solution:
    def primeSum(self, N):
        # code here
        return sum([int(i) for i in str(N) if i == '2' or i == '3' or i == '5' or i == '7'])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.primeSum(N))
# } Driver Code Ends