#User function Template for python3

class Solution:
    def acceptedProposals (self,arr, n):
        # your code here
        arr.sort()
        return arr[-2],arr[1]