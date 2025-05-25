#User function Template for python3

class Solution:
    def getPPS(self, a, b):
        # code here 
        def isPrime(num):
            if num < 2:
                return False
            
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True
                
        return sum(num for num in range(a,b+1) if isPrime(num) and str(num) == str(num)[::-1])