#User function Template for python3

class Solution:
    def printTriangle(self, n):
        # Code here
        for row in range(1,2*n):
            if row > n:
                totalRow = 2*n - row
            else:
                totalRow = row
            for col in range(1,totalRow+1):
                print("*",end = " ")
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