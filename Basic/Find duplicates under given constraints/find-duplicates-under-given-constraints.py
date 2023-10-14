#User function Template for python3

def findDuplicate(A):
    # Your code goes here
    for i in A:
        if A.count(i)==5:
            return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        # n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findDuplicate(a))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends