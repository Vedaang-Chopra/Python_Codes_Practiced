def Tobinary(n):
    ch=False
    r=[]
    while(ch==False):
        r.append(n % 2)
        n=n//2
        if n//2==1:
            r.append(n%2)
            r.append(1)
            ch=True
    return r

n=int(input())
a=(Tobinary(n))
for i in range(0,len(a)):
    a[i]=str(a[i])
#print(a)
string=a.pop()
for i in range(0,len(a)):
    string1=a.pop()
    string=string+string1
#print(string)
binaryno=int(string)
print(binaryno)