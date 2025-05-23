#User function Template for python3
def fibonacci(n):
    #your code here
    # return nth fibonacci element
    a, b = 0, 1
    for _ in range(2,n+1):
        a, b = b, a+b
    return b