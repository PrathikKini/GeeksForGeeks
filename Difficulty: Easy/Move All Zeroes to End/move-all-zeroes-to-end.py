#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	n = len(arr)
    	pos_idx = 0
    	
    	for i in range(n):
    	    if arr[i] != 0:
    	        arr[pos_idx] = arr[i]
    	        pos_idx+=1
    	
    	for i in range(pos_idx,n):
    	    arr[i] = 0
    	