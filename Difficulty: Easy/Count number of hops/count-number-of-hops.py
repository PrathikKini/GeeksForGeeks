#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        if n<=1:
            return 1
        elif n == 2:
            return 2
        else:
            # code here
            first, second, third = 1, 1, 2
            for _ in range(3,n+1):
                next_step = first + second + third
                first = second
                second = third
                third = next_step
            return next_step