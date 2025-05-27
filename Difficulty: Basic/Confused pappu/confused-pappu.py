#User function Template for python3

class Solution:

    def findDiff(self, amount):
        # code here
        l = []
        for i in str(amount):
            if i == '6':
                l.append('9')
            else:
                l.append(i)
        return int("".join(l)) - amount