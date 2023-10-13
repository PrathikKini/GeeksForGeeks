#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for rows in range(1, N+1):
            for cols in range(1,rows+1):
                if (rows + cols) % 2 == 0:
                    print("1", end = ' ')
                else:
                    print("0", end = ' ')
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends