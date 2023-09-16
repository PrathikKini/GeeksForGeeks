#User function Template for python3

def countOfElements( a, n, x):
    left , count = 0, 0
    right = n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] <= x:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends