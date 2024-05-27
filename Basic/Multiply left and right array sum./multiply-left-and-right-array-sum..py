#User function Template for python3

def multiply (arr, n) : 
    #Complete the function
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    sum_l = sum(l)
    sum_r = sum(r)
    return sum_l * sum_r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends