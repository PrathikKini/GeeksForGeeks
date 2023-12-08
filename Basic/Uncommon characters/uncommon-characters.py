#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        s = set([i for i in A if i not in B])
        t = set([i for i in B if i not in A])
        if len(s) > 0 or len(t) > 0:
            return "".join(sorted(s.union(t)))
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends