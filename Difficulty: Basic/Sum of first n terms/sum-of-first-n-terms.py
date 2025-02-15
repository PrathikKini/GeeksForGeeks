#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        return sum(i*i*i for i in range(1,n+1))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends