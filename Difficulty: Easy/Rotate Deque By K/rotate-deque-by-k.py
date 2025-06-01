#User function Template for python3
from collections import deque
#Function to rotate deque by k places in anti-clockwise direction.
def left_Rotate_Deq_ByK(deq,k):
    #code here
    return deq.rotate(-k)
 
#Function to rotate deque by k places in clockwise direction.   
def right_Rotate_Deq_ByK(deq,k):
    #code here
    return deq.rotate(k)