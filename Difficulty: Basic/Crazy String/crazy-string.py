#User function Template for python3

class Solution:

    def getCrazy(self, S):
        # code here
        res = [S[0]]
        is_upper = S[0].isupper()
        
        for i in range(1,len(S)):
            if is_upper:
                if i % 2 == 0:
                    res.append(S[i].upper())
                else:
                    res.append(S[i].lower())
            else:    
                if i % 2 == 0:
                    res.append(S[i].lower())
                else:
                    res.append(S[i].upper())
        
        return "".join(res)