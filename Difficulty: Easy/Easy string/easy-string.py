#User function Template for python3

class Solution:

    def transform(self, S):
        # code here
        comp_str = ""
        count = 1
        S = S.lower()
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                count+=1
            else:
                comp_str+=str(count) + S[i-1]
                count = 1
        comp_str+=str(count) + S[-1]
        return comp_str 