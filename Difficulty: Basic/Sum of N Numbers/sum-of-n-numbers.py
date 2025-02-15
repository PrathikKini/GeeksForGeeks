#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def nSum(n):
    
    ans = 0
    
    #Write your code here to calculate and return sum of n number.
    for i in range(1,n+1):
        ans+=i
    
    return ans

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        ans = nSum(n)
        print(ans)
        print("~")
# } Driver Code Ends