class Solution:
    def printTable(self, n):
        multiplier = 10
        while(multiplier>0):
            # Code here
            print(multiplier*n,end = " ")
            multiplier-=1
        print()