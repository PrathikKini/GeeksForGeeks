#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        start_ind = end_ind = -1
        for i in range(N):
            if a[i] == key:
                start_ind = i
                break
            
        for i in range(N-1,-1,-1):
            if a[i] == key:
                end_ind = i
                break
        
        return start_ind, end_ind


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends