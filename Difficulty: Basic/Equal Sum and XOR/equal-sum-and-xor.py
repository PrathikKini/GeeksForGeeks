# You are required to complete this fucntion
# Function should return the an integer
def countValues(n):
    # Code here
    cnt = 0
    for i in range(n+1):
        if (n+i == n^i):
            cnt+=1
    return cnt