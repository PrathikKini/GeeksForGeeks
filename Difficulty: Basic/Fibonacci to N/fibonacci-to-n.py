#User function Template for python3

class Solution:
    def nFibonacci(self,N):
        #code here
        a = 0
        b = 1
        l = [a]
        while a <= N:
            l.append(b)
            a, b = b, a+b
        
        if l[-1] > N:
            l.pop()
            
        return l
        