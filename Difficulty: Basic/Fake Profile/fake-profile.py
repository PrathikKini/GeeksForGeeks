#User function Template for python3

class Solution:

    def solve(self, a):
        # code here
        vowels = 'aeiou'
        l = set()
        for i in a:
            if i not in vowels:
                l.add(i)
        return "SHE!" if len(l) % 2 == 0 else "HE!"