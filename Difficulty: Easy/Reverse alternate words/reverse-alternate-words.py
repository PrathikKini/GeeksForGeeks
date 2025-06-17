#User function Template for python3

class Solution:
    from itertools import zip_longest
    def reverseAlternate(self, Str):
        # code here
        org_l = [i for i in Str.split()[::2]]
        sec_l = [i[::-1] for i in Str.split()[1::2]]
        return " ".join(x for pair in self.zip_longest(org_l,sec_l) for x in pair if x is not None)