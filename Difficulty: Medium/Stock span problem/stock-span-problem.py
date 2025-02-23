#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        #write code here
        stack = []
        span = [0] * len(arr)
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            span[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)
        return span

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends