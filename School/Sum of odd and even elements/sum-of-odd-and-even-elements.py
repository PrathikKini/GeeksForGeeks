#User function Template for python3

class Solution:
	def find_sum(self, n):
		# Code here
        even = n//2
        odd = n-n//2
        return odd**2,even*(even+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_sum(n)
		for _ in ans:
			print(_, end=" ")
		print()
# } Driver Code Ends