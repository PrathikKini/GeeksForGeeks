#User function Template for python3

class Solution:
    def difProblem(self, N):
        # code here 
        non_decreasing = all(N[i] <= N[i+1] for i in range(len(N)-1))
        non_increasing = all(N[i] >= N[i+1] for i in range(len(N)-1))
        return 1 if non_decreasing or non_increasing else 0 