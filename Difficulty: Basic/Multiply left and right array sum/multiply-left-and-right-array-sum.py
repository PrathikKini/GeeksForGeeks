#User function Template for python3

class Solution:
    def multiply(self, arr):
        # Code here
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        sum_l = sum(l)
        sum_r = sum(r)
        return sum_l * sum_r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.multiply(arr))
        print("~")

# } Driver Code Ends