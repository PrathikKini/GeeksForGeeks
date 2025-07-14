#User function Template for python3



class Solution:
    def isprime(self, num):
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    def minNumber(self, arr,n):
        # code here
        total = sum(arr)
        x = 0
        while True:
            if self.isprime(total+x):
                return x
            x += 1
            