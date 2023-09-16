#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		s = sorted(v)
		n = len(v)
		if n % 2 == 0:
		    x = (s[n//2-1]+s[n//2])//2
		    return x
		else:
		    return s[n//2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends