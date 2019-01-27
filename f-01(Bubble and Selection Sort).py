# Selection Sort
# Given a random integer array. Sort this array using selection sort.
# Change in the input array itself. You don't need to return or print elements.
# Input format :
#
# Line 1 : Array Size
#
# Line 2 : Array elements (separated by space)
#
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
# Sample Input 2:
# 5
# 9 3 6 2 0
# Sample Output 2:
# 0 2 3 6 9


# Bubble Sort-Code
def bubble_sort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j] >= a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
            print(a[j], a[j+1], max(a[j], a[j+1]))
    return a


# Selection Sort-Code
def selection_sort(a):
    t = []
    for i in range(0, len(a)):
        k = min(a[0:len(a)])
        a.remove(k)
        t.append(k)
    return t

print("Enter No. of Elements in List:")
d =int(input())
print("Enter elements of list(seperated by space):")
n = input()
n = n.strip()
b = n.split(" ")
for i in range(0, d):
    b[i] = int(b[i])
print(selection_sort(b))
print(bubble_sort(b))




