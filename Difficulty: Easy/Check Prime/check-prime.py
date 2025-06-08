#User function Template for python3

def prime(n):
    
    # code here to check for prime.
    # return True or False
    if n <= 1:
        return False
    for num in range(2,int(n**0.5)+1):
        if n % num == 0:
            return False
    return True