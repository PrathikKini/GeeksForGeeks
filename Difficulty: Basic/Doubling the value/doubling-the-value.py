#User function Template for python3

class Solution:
    def solve(self,n : int, a : list, b : int):
        # Complete this function
        
        while b in a:
            b*=2
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , b = map(int, input().split())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.solve(n, arr, b))
        print("~")
# } Driver Code Ends