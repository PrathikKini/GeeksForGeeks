#User function Template for python3

class Solution:
    def countDivisors(self, n):
        # code here
        return sum(n%i==0 and i%3==0 for i in range(1,n+1))

#{ 
 # Driver Code Starts
#Initial Template for Python 3#Back-end complete function Template for Python 3#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countDivisors(N))

# } Driver Code Ends