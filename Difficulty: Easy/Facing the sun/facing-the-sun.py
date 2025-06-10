#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        cursum = height[0]
        count = 1
        for i in range(1,len(height)):
            if cursum < height[i]:
                cursum = height[i]
                count+=1
        return count