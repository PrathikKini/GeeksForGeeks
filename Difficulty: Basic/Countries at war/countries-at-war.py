#User function Template for python3


class Solution:

    def countryAtWar(self, arr1, arr2):
        #  code here
        arr1_cnt = 0
        arr2_cnt = 0
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                arr1_cnt+=1
            elif arr1[i] < arr2[i]:
                arr2_cnt+=1
            else:
                continue
        
        if arr1_cnt > arr2_cnt:
            return "A"
        elif arr1_cnt < arr2_cnt:
            return "B"
        else:
            return "DRAW"