#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for i in range(1, N + 1):
            # Print spaces before the stars
            for j in range(N, i, -1):
                print(" ", end="")
        
            # Print the stars
            for k in range(1, i * 2):
                print("*", end="")
        
            # Move to the next line after each row
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends