#User function Template for python3
class Solution:
	def getXor(self, A, N):
		# code here
		total_xor = 0
		for i in A:
		    total_xor ^= i
		result = [total_xor ^ num for num in A]
		return result