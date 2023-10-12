# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    s=str(arr)
    return s.count(str(k))

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends