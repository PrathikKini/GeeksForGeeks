#User function Template for python3


def lessThan(arr, k):
    # write your code below to append all numbers to ans which are less than k
    return [arr[i] for i in range(len(arr)) if arr[i] < k]
