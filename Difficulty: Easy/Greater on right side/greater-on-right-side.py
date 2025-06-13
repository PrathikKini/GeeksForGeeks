#User function Template for python3
class Solution:

	def nextGreatest(self,arr):
		# code  here
		max_result = -1
		for i in range(len(arr)-1,-1,-1):
		    current = arr[i]
		    arr[i] = max_result
		    max_result = max(max_result,current)
		return arr