#User function Template for python3

class Solution:
    def getSmallestDivNum(self, n): 
        # code here 
        from math import gcd
        lcm = 1
        for i in range(1,n+1):
            lcm = (lcm * i) // gcd(lcm,i)
        return lcm

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob = Solution()
        print(ob.getSmallestDivNum(n))
        print("~")
# } Driver Code Ends