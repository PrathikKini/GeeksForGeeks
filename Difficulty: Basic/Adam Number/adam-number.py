#User function Template for python3

class Solution:
    def checkAdamOrNot(self, N):
        # code here 
        a = N*N
        b = int(str(N)[::-1]) * int(str(N)[::-1])
        return "YES" if str(a) == str(b)[::-1] else "NO"