#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor = -1
        ceil = -1
        for num in arr:
            if num <= x:
                floor = max(num,floor)
            if num >= x:
                if ceil == -1:
                    ceil = num
                else:
                    ceil = min(ceil,num)
        return [floor,ceil]