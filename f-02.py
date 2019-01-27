
# print('Enter the number for Pattern<=10:')
n=int(input())
ch=False
while ch==False:
    if n<=10:
     # print("Number accepted..........")
        ch=True
    else:
      # print("Write proper number!!!!!!!!!!!!!!!!!")
        n=int(input())
z=(n*2)-2
c=0
if n<10:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>=j:
                print(j,end=" ")
                c=j
        for t in range(1,z*2+1):
            print(" ",end="")
        for k in range(c,0,-1):
            print(k,end=" ")
        z=z-2
        print()
elif n==10:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>=j:
                print(j,end=" ")
                c=j
        for t in range(1,z*2+1):
            print(" ",end="")
        if c<n:
            print(" ", end="")
            print(" ", end="")

        for k in range(c,0,-1):
            print(k,end=" ")
        z=z-2
        print()
# print("The Pattern is Printed............................................................")


