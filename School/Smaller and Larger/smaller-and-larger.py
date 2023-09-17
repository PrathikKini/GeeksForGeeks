#User function Template for python3
class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if arr[i]<=x:
                cnt1+=1
            if arr[i]>=x:
                cnt2+=1
        return cnt1,cnt2


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends