#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		if len(arr) < 2:
		    return -1 
		    
		first_max = second_max = float('-inf')
		
		for num in arr:
		    if num > first_max:
		        second_max = first_max
		        first_max = num
		    elif num > second_max and num != first_max:
		        second_max = num
		        
		if second_max == float('-inf'):
		    return -1
		return second_max
		        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends