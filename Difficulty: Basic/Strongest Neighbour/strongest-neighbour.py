#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to find maximum for every adjacent pairs in the array.
def maximumAdjacent(sizeOfArray, arr):
    
    # Your code here
    # Function should print max of all adjacents
    print(*[max(arr[i-1],arr[i]) for i in range(1,len(arr))],end = " ")
    


#{ 
 # Driver Code Starts.
    
# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        maximumAdjacent(sizeOfArray, arr)
        
        print()
        
        testcases -= 1

        print("~")
if __name__ == '__main__':
    main()
    
    
# } Driver Code Ends