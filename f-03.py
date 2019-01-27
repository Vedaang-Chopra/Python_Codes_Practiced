print('Enter The String:')
s=input()
s1=""
b=-1
e=s.split()
for i in e:
    for j in range(-1,-len(i)-1,-1):
        s1=s1+i[j]

    s1=s1+" "
print("Reversed string is:",end=" ")
print(s1)





