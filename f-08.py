def oddcalc(n):
    d = n // 2
    d = d + 1
    c = n * d
    return c
def evencalc(n):
    a = n // 2
    b = n * a + a
    return b
def mincalc(n):
    s=0
    for i in range(1,n):
        s=s+i
    return s+1
def pattern (n,e):
    print(n,e)
    c,d=0,0
    for i in range(1,n+1):
        if i%2==0:
           c=evencalc(i)
        else:
           c=oddcalc(i)
        d=mincalc(i)
        if i==1:
            print('1')
        elif i>1 and i%2==0:
            for j in range(c,d+1,-1):
                print(j,end=" ")
        elif i>1 and i%2!=0:
            for j in range(d,c+1):
                print(j,end=" ")
        print()

n=int(input())
if n%2==0:
    pattern(n,evencalc(n))
else:
    pattern(n,oddcalc(n))
