# Array Equilibrium Index
# Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
# Element at index i is not included in either part.
# If more than one equilibrium index is present, you need to return the first one. And return -1 if no equilibrium index is present.
# Input format :
#
# Line 1 : Size of input array
#
# Line 2 : Array elements (separated by space)
#
# Sample Input:
# 7
# -7 1 5 2 -4 3 0
# Output:
# 3
def equiindex(a):
    s1 = 0
    s2 = 0
    flag = False
    d = []
    # print(a)
    for k in a:					#Calculation of total sum
        s2 = k + s2
    #print("s2",s2)
    for i in range(0, len(a)):
        s2=s2-a[i]
        s1=s1+a[i]
        #print(a[i],s1,s2,s2-a[i])
        if (s1-a[i]) ==(s2) :	# Comparison where total and leftsum is being subtracted
            flag = True
            d.append(i)
       # print(d)

    return d, flag


size = int(input())
n = input()
n = n.strip()
b = n.split(" ")
for i in range(0, size):
    b[i] = int(b[i])
a, booleanval = equiindex(b)
if booleanval == True:
    print(a[0])
else:
    print("-1")