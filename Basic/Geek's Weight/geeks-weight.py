#User function Template for python3

class Solution:
	def total_Money(self, n, k):
		# Code here
		m = n // k
		return k * m * (m + 1) // 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		ob = Solution()
		ans = ob.total_Money(n, k)
		print(ans)
# } Driver Code Ends