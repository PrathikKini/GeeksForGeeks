#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        # code here
        return "".join([v for i,v in enumerate(S) if i%2==0])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends