def prime(n):
    flag=True
    if n==1:
        print('No output')
    if n==2:
        print('2')
    if n==3:
        print('2')
        print('3')
    else:
        print('2')
        print('3')
        for i in range(4,n+1):
            flag=False
            for j in range(2,i):
                if i%j==0 :
                    flag=True
            if flag==False:
                print(i)


n=int(input())
prime(n)
