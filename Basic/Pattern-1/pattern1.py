#User function Template for python3

class Solution:
    def findThePattern(self, N):
        # code her
        result = []
        ch = ord('A')
        
        for i in range(N):
            row_str = ''
            for j in range(N):
                if i == 0 or j == 0 or i == N -1 or j == N -1:
                    row_str += chr(ch)
                    ch+=1
                else:
                    row_str += '$'
            result.append(row_str)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr=ob.findThePattern(N)
        for i in ptr:
            print(i)
# } Driver Code Ends