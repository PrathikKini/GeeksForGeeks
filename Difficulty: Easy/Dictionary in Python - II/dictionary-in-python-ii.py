# Function to check if pair
# with given sum exists
def pair_sum(dict, arr, sum):
    # code here
    # Hint: You can use 'in' to find if any key is in dict
    prevMap = {}
    for num in arr:
        diff = sum - num
        if diff in prevMap:
            return True
        prevMap[num] = True
    return False
        
    