#User function Template for python3

class Solution:
    def oddAndEven(self,S):
        odd,even=0,0
        for i in range(len(S)):
            if i%2:
                even+=int(S[i])
            else:
                odd+=int(S[i])
        return 1 if even==odd else 0  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.oddAndEven(S))
# } Driver Code Ends