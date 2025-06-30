#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        max_profit = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                max_profit += arr[i] - arr[i-1]
        return max_profit