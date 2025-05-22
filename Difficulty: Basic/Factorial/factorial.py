#User function Template for python3


def nFactorial(n):

    ans = 1

    #Write your code below
    for i in range(2,n+1):
        ans *= i

    return ans
