class Solution:
    def calculateFriendliness(self, arr):
        # code here
        sum_amt = 0
        for i in range(1,len(arr)):
            sum_amt += abs(arr[i-1]-arr[i])
        sum_amt += abs(arr[0]-arr[-1])
        return sum_amt