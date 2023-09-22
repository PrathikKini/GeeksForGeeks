#User function Template for python3
class Solution:
    def isInRange (ob,N):
        # code here 
        if N == 1:
            return "one"
        elif N == 2:
            return "two"
        elif N == 3:
            return "three"
        elif N == 4:
            return "four"
        elif N == 5:
            return "five"
        elif N == 6:
            return "six"
        elif N == 7:
            return "seven"
        elif N == 8:
            return "eight"
        elif N == 9:
            return "nine"
        elif N == 10:
            return "ten"
        else:
            return "not in range"
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.isInRange(N))
# } Driver Code Ends