#User function Template for python3

"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""
def findFrequency (arr, n, x):
    # Your Code Here
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = 1 + d.get(arr[i],0)
    for k, v in d.items():
        if k == x:
            return v
    return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    print (findFrequency (arr, n, x))
    

# } Driver Code Ends