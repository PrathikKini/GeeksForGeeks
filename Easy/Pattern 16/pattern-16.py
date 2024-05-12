#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        c = 1
        for i in range(65,65+N):
            print(chr(i)*c)
            c+=1


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