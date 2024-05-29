#User function Template for python3
class Solution:
    def repeatedSumOfDigits (self,N):
        # code here 
        while N >= 10:
            N = sum(int(i) for i in str(N))
        return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
      
        ob = Solution()
        print(ob.repeatedSumOfDigits(N))
# } Driver Code Ends