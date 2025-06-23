#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        stack = []
        for num in arr:
            if not stack:
                stack.append(num)
            else:
                top = stack[-1]
                if ((top<0 and num > 0) or (top>0 and num<0) or 
                (num==0 and top < 0) or (top==0 and num < 0)):
                    stack.pop()
                else:
                    stack.append(num)
        return stack