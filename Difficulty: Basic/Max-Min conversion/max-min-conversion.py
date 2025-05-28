#User function Template for python3

def performOperation(n):
    #code here
    max_list = [i.replace('5','6') for i in str(n)]
    min_list = [i.replace('6','5') for i in str(n)]
    max_val = int("".join(max_list))
    min_val = int("".join(min_list))
    return max_val + min_val