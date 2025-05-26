#User function Template for python3
def LCM(a,b):
    # Your code here
    def gcd(a,b):
        while b:
            a, b = b, a % b
        return a
    
    return abs(a*b) // gcd(a,b)