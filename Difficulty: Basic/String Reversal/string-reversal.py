#User function Template for python3

class Solution:
    def reverseString(self, s):
        # code here
        seen = set()
        lst = []
        
        for ch in reversed(s):
            if ch != ' ' and ch not in seen:
                seen.add(ch)
                lst.append(ch)
            
        return "".join(lst)
