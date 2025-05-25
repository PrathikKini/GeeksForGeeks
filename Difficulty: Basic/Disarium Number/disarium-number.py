#User function Template for python3

class Solution:
    def isDisarium(self, N):
        # code here 
        return 1 if sum(int(num)**i for i,num in enumerate(str(N),1)) == N else 0