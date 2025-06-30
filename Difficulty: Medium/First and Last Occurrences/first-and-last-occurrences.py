#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        def first_occurence(arr,x):
            low = 0
            high = len(arr) - 1
            res = -1
            while low <= high:
                mid = (low+high) // 2
                if arr[mid] == x:
                    res = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
            
        def last_occurence(arr,x):
            low = 0
            high = len(arr) - 1
            res = -1
            while low <= high:
                mid = (low+high) // 2
                if arr[mid] == x:
                    res = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
            
        return [first_occurence(arr,x),last_occurence(arr,x)]