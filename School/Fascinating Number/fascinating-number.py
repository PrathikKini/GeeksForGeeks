#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
        if n>99:
            prod = str(n)+str(n*2)+str(n*3)
        return "".join(sorted(prod)) == "123456789"
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends