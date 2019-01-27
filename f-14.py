def largestsubstring(string):
    d=[]
    for i in range(0,len(string)):
        substr1=string[i]
        for j in range(i+1,len(string)):
            if string[i]==string[j]:
                break
            else:
                substr1=substr1+string[j]
        d.append(substr1)
    #print(d)
    string4=""
    flag=True
    for i in range(0,len(d)*len(string)):
        string3=d.pop()
        flag=True
        #print(string3)
        for j in range(0, len(string3) - 1):
            for k in range(j + 1, len(string3)):
               # print(string3[j], string3[k])
                if string3[j] == string3[k]:
                    string4 = string3[0:k]
                    flag=False
                    break
        #print(string3)
        if flag==True:
            d.insert(0,string3)
        if(flag==False):
            d.append(string4)
    #print(d)
    c1=0
    c=[]
    e=[]
    for i in range(0,len(d)):
        for j in range(0,len(d[i])):
            c1=c1+1
        c.append(c1)
        c1=0
    for i in range(0,len(c)):
        if max(c)==c[i]:
             e.append(d[i])
    return e
n=input()
a=(largestsubstring(n))
#print(a)
c=[]
d=0
flag=True
length=0
for i in a:
    c.append(n.find(i))
for i in range(0,len(c)):
    if min(c)==c[i]:
        print(a[i])