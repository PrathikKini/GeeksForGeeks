class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        res = []
        arr.sort()
        left, right = 0 , len(arr) - 1
        
        while left <= right:
            if left != right:
                res.append(arr[right])
                res.append(arr[left])
            else:
                res.append(arr[right])
            left += 1
            right -= 1
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
