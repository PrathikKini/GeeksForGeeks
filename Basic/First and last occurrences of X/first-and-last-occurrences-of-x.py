#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        # Code here
        a = []
        for i in range(len(arr)):
            if arr[i] == x:
                a.append(i)
        if a:
            return [a[0],a[-1]]
        else:
            return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends