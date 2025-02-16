#User function Template for python3

class Solution:
    def closestNumber(self, n , m):
        # code here 
        low=n//m*m;high=((n//m)+1)*m
        if abs(abs(n)-abs(low))<abs(abs(n)-abs(high)):
            return low
        elif abs(abs(n)-abs(low))>abs(abs(n)-abs(high)):
            return high
        else:
            return low if abs(low)>abs(high) else high
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        M = int(input())

        ob = Solution()
        print(ob.closestNumber(N, M))
        print("~")

# } Driver Code Ends