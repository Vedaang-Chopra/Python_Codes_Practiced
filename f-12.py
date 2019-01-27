def leaderarr(n):
    d=[]
    for i in range(0, len(n)):
        flag=True
        for j in range(i+1,len(n)):
            #print(n[i],n[j],flag)
            if n[i]>=n[j]:
                flag=True
            else:
                flag=False
                break
        if flag==True:
            d.append(n[i])
    return d


size = int(input())
n = input()
n = n.strip()
b = n.split(" ")
for i in range(0, size):
    b[i] = int(b[i])
a=(leaderarr(b))
for i in a:
    print(i,end=" ")