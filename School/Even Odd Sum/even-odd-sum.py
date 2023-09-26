#User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        even_sum = 0
        odd_sum = 0
        for i,v in enumerate(Arr,1):
            if i%2==0:
                even_sum+=v
            else:
                odd_sum+=v
        return (odd_sum,even_sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])
# } Driver Code Ends