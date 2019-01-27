def fib(n):
    a = 0
    b = 1
    c=0
    s=0
    d=[]
    if n == 0:
        d.append(0)
    elif n == 1:
       d.append(0)
    else:
        s=2
        while(c<=n):
            c = a + b
            a = b
            b=c
            if s%3==0:
                d.append(c)
            s=s+1

    print(d)
    s=0
    for i in d:
       if i<=n:
           s=s+i
    return s
n = int(input())
ch=True
while(ch==True):
    if(n>=1 and n<=1000000):
        print(fib(n))
        ch=False
    else:
        n=int(input())
