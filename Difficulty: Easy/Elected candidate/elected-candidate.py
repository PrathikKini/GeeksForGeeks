#User function Template for python3

class Solution:
	def electionWinner(self, arr):
		# code here
		countArr = {}
		for i in range(len(arr)):
		    countArr[arr[i]] = 1+countArr.get(arr[i],0)
		max_val = max(countArr.values())
		return max(name for name, cnt in countArr.items() if max_val == cnt)