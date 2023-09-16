#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        fibo_series = []
        
        if n>=1:
            fibo_series.append(1)
        if n>=2:
            fibo_series.append(1)
               
        for i in range(2,n):
            next_n = fibo_series[i-1] + fibo_series[i-2]
            fibo_series.append(next_n)
        return fibo_series

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends