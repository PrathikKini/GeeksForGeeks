#User function Template for python3
class Solution:
	def numberPattern(self, N):
		# code here
        arr = []
        p = 0
        for i in range(N):
            k = ''
            for j in range(i+1):
                k += str(j+1)
            for j in range(i):
                k += str(p-j)
            p += 1
            arr.append(k)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        res = ob.numberPattern(N)
        for each in res:
            print(each, end=" ")
        print()
        

# } Driver Code Ends