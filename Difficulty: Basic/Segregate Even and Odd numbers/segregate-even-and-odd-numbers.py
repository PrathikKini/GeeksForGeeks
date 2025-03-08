#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
		# code here
        evens = [x for x in arr if x % 2 == 0]
        odd = [x for x in arr if x % 2 != 0]
        
        evens.sort()
        odd.sort()
        
        arr[:len(evens)] = evens
        arr[len(evens):] = odd
        
        return arr
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

        print("~")

# } Driver Code Ends