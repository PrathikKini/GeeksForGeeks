#User function Template for python3
class Solution:
	def removeCharacters(self, S):
		# code here
        return "".join([i for i in S if i.isdigit()])

                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeCharacters(s)
		
		print(answer)


# } Driver Code Ends