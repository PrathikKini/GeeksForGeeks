#User function Template for python3

def isSubset( a1, a2, n, m):
    dict1 = {}
    for i in range(len(a1)):
        dict1[a1[i]] = 1 + dict1.get(a1[i],0)
        
    for ele in a2:
        if ele in dict1 and dict1[ele] > 0:
            dict1[ele] -= 1
        else:
            return 'No'
    return 'Yes'
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends