def factorialzero(n):
    f=5
    c=1
    d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1,11):
        c=c*f
        d[i]=n//c
    s=0
    for i in d:
        s=s+i
    return s

n=int(input())
ch=True
while(ch==True):
    if(n>=0 and n<100000000000):
        print(factorialzero(n))
        ch=False
    else:
        n=int(input())