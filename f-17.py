def rowsum(arr,n,m):
    row=[]
    s=0
    for i in range(0,n):
        s=0
        for j in range(0,m):
            s=s+arr[i][j]
        row.append(s)
    val=max(row)
    for i in range(0,len(row)):
        if(row[i]==val):
            return i,val
def colsum(arr,n,m):
    column=[]
    s=0
    for j in range(0,m):
        s=0
        for i in range(0,n):
            #print(j,i,arr[i][j])
            s=s+arr[i][j]
        column.append(s)
    val=max(column)
    for i in range(0,len(column)):
        if(column[i]==val):
            return i,val


a=input()
b=a.strip().split(' ')
n=int(b[0])
m=int(b[1])
c=input()
d=c.strip().split(' ')
for i in range(0,len(d)):
  d[i]=int(d[i])
d=[[d[i*m+j] for j in range(0,m)] for i in range(0,n)]
ri,rv=rowsum(d,n,m)
ci,cv=colsum(d,n,m)
if rv>cv:
    print('row',ri,rv)
elif rv<cv:
    print('col',ci,cv)
else:
    print('row',ri,rv)
