def printPat(n):
    #Code here
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            for k in range(1,i+1):
                print(j,end = ' ')
        print('$',end='')
    print()


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends