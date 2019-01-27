'''

def spiralprint(arr,m,n):
    if m==n:
        if m%2!=0:
            c = 0
            d = 0
            flag = False
            for k in range(0, (m // 2)+1):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
                    if 0+c == (m // 2)+1:
                        flag = True
                        break
                if flag == True:
                    break
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
                for j in range(0 + c, 1 + c):
                    for i in range(n - 2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
                c = c + 1
                d = d - 1
        else:
            c = 0
            d = 0
            flag = False
            for k in range(0, (m // 2)+1):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
                    if n-2+d == (m // 2) + 1:
                        flag = True
                        break
                if flag == True:
                    break
                for j in range(0 + c, 1 + c):
                    for i in range(n - 2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
                c = c + 1
                d = d - 1
    elif m<n:
        if m%2!=0:
            c = 0
            d = 0
            flag = False
            for k in range(0, (m // 2)+1):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
                if 0 + c == (m // 2) :
                    flag = True
                    break
                #print('Start row loop')
                if flag == True:
                    break
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                #print('End column loop')
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
                #print('End row loop')
                for j in range(0 + c, 1 + c):
                    for i in range(m - 2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
                #print('Start column loop')
                c = c + 1
                d = d - 1
        else:
            c = 0
            d = 0
            flag = False
            for k in range(0, (m // 2)):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
                #print('Start row loop')
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                #print('End column loop')
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
                    if n-2+d == (m // 2) + 1:
                        flag = True
                        break
                #print('End row loop')
                if flag == True:
                    break
                for j in range(0 + c, 1 + c):
                    for i in range(m-2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
                #print('Start column loop')
                c = c + 1
                d = d - 1
    else:
        if n % 2 != 0:
            c = 0
            d = 0
            flag = False
            for k in range(0, (n // 2)+1):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
             #   #print('Start row loop')
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                    if 1+c == (n // 2)+1:
                        flag = True
                        break
              #  #print('End column loop')
                if flag == True:
                    break
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
               # #print('End row loop')
                for j in range(0 + c, 1 + c):
                    for i in range(m - 2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
               # #print('Start column loop')
                c = c + 1
                d = d - 1
        else:
            c=0
            d=0
            flag=False
            for k in range(0, (n // 2)+1):
                for i in range(0 + c, 1 + c):
                    for j in range(0 + c, n + d):
                        print(arr[i][j], end=" ")
                for j in range(n - 1 + d, n + d):
                    for i in range(1 + c, m + d):
                        print(arr[i][j], end=" ")
                for i in range(m - 1 + d, m + d):
                    for j in range(n - 2 + d, -1 + c, -1):
                        print(arr[i][j], end=" ")
                for j in range(0 + c, 1 + c):
                    for i in range(m - 2 + d, 0 + c, -1):
                        print(arr[i][j], end=" ")
                if m - 2 + d == (n // 2)+1:
                    flag = True
                    break
                if flag == True:
                    break
                c = c + 1
                d = d - 1
'''
def spiralprint(arr,m,n):
    rs=0
    re=m-1
    cs=0
    ce=n-1
    d=m*n
    c=0
    while(c<d):
        #print('loop1',rs,cs,re,ce,c)
        for i in range(cs,ce+1):
            print(arr[rs][i],end=" ")
            c=c+1
        rs=rs+1
        if c == d:
            break
        #print('\n loop2',rs,cs,re,ce,c)
        for i in range(rs,re+1):
            print(arr[i][ce],end=" ")
            c = c + 1
        ce=ce-1
        #print('\n loop3',rs,cs,re,ce,c)
        if c == d:
            break
        for i in range(ce,cs-1,-1):
            print(arr[re][i],end=" ")
            c = c + 1
        re=re-1
        if c == d:
            break
        #print('\n loop4',rs,cs,re,ce,c)
        for i in range(re, rs-1,-1):
            print(arr[i][cs],end=" ")
            c = c + 1
        cs=cs+1
        if c == d:
            break
a=input()
b=a.strip().split(' ')
n=int(b[0])
m=int(b[1])
for i in range(0,len(b)):
  b[i]=int(b[i])
b.remove(n)
b.remove(m)
d=[[b[i*m+j] for j in range(0,m)] for i in range(0,n)]
spiralprint(d,n,m)
