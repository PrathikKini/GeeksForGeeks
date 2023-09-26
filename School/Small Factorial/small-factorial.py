#User function Template for python3

class Solution:
	def find_fact(self, n):
		# Code here
        res = 1
        for i in range(2,n+1):
            res*=i
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_fact(n)
		print(ans)

# } Driver Code Ends