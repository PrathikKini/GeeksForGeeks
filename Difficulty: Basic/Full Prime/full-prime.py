#User function Template for python3

class Solution:
    def fullPrime(self,N):
        #code here
        prime_digit = {2,3,5,7}
        for i in range(2,int(N**0.5)+1):
            if N % i == 0:
                return 0
        return 1 if all(int(i) in prime_digit for i in str(N)) else 0
            