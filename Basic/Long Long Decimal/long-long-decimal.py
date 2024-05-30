#User function Template for python3
from decimal import *
class Solution:
	def upto_K_places(self, k):
		# Code here
		
		if k >23:
            getcontext().prec = k + 4
        result = Decimal(355) / Decimal(113)
        ko = str(result)[:k+2:]
        # print(ko, result)
        return (ko)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		k = int(input())
		ob = Solution()
		ans = ob.upto_K_places(k)
		print(ans)
# } Driver Code Ends