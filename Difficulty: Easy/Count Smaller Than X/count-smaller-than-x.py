#User function Template for python3

class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        cnt = 0
        for i in arr:
            if i < x:
                cnt+=1
        return cnt