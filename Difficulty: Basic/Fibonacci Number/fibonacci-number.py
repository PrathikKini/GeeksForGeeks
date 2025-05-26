#User function Template for python3
#Back-end complete function Template for Python 3
n = int(input())

########### Write your code below ###############
a = 0
b = 1
l = [0,1]
for i in range(2,n+1):
    c = a + b
    a = b
    b = c
    l.append(b)
########### Write your code above ###############
print(l[-1])
