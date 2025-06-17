def LargButMinFreq(arr,n):
    #code here
    countA = {}
    for i in range(len(arr)):
        countA[arr[i]] = countA.get(arr[i],0) + 1
    min_val = min(countA.values())
    return max([k for k,v in countA.items() if min_val == v])