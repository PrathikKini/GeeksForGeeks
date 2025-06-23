from math import sqrt
class Solution:
    def isPrime(self, n : int) -> str:
        # code here
        if n == 1:
            return "No"
        for i in range(2,int(sqrt(n))+1):
            # Write your logic here
            if n % i == 0:
                return "No"
        return "Yes"
            # Return "Yes" if n is prime, else return "No"
            #*n is prime only if it is not divisible by any i , We will not reach till n and 1 is already discarded*/

            #return  Yes if n is a prime number ,else return No