#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        digits = [int(i) for i in str(N)]
        sum_n = sum(digits)
        if str(sum_n) == str(sum_n)[::-1]:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends