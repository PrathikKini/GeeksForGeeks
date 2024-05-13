#User function Template for python3

class Solution:
	def sumofproduct(self, n):
		# Code here
		total = 0
		for i in range(1, n+1):
            total += i * (n//i)
        return total
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
# } Driver Code Ends