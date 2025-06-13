class Solution:
    def arrangeOddAndEven(self, arr):
        # Your code goes here
        from itertools import zip_longest
        even = [x for x in arr if x%2 == 0]
        odd = [x for x in arr if x%2 != 0]
        return [x for pair in zip_longest(even,odd) for x in pair if x is not None]