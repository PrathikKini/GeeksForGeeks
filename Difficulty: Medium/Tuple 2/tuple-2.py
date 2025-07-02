#User function Template for python3

def sequence(tup):
    # code here to return tuple containing whole sequences
    d = tup[1] - tup[0]
    return tup + (tup[-1]+d,tup[-1]+(2*d),tup[-1]+(3*d))