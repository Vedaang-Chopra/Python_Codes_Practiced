'''
#def treepath(arr1,arr2):
    iarr1 = []
    iarr2 = []
    varr = []
    s=0
    sum1=[]
    sum2=[]
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                iarr1.append(i)
                iarr2.append(j)
                varr.append(arr1[i])
            elif arr1[i]<arr2[j]:
                continue
            else:
                break
    for i in range(0,len(iarr1)):
        if i==0:
            for j in range(0,iarr1[i]):
                s=s+arr1[j]
            sum1.append(s)
            s=0
        else:
            for j in range(iarr1[i-1],iarr1[i]):
                s=s+arr1[j]
            sum1.append(s-varr[i-1])
            s=0
    s=0
    for i in range(0,1):
        for j in range(max(iarr1)+1,len(arr1)):
            s=s+arr1[j]
        sum1.append(s)
        s=0
    for i in range(0, len(iarr2)):
        if i == 0:
            for j in range(0, iarr2[i]):
                s = s + arr2[j]
            sum2.append(s)
            s = 0
        else:
            for j in range(iarr2[i - 1], iarr2[i]):
                s = s + arr2[j]
            sum2.append(s-varr[i-1])
            s = 0
    s = 0
    for i in range(0, 1):
        for j in range(max(iarr2) + 1, len(arr2)):
            s = s + arr2[j]
        sum2.append(s)
        s = 0
    a=max(len(sum1),len(sum2))
    e=[]
    for i in range(0,a):
        e.append(max(sum1[i],sum2[i]))

    s=0
    for i in e:
        s=s+i
    for i in varr:
        s=s+i
    return s
'''
def treepath(arr1,arr2):
    s1=0
    s2=0
    maxsum=0
    i=0
    j=0
    c=[0,0]
    while( i<len(arr1) and j<len(arr2)):
        #print(i,j,s1,s2,maxsum,end="    ")
        if(arr1[i]<arr2[j]):
            s1=s1+arr1[i]
            i=i+1
        elif arr2[j]<arr1[i]:
            s2=s2+arr2[j]
            j=j+1
        else:
            maxsum=maxsum+max(s1,s2)
            s1=0
            s2=0
            c[0]=i
            c[1]=j
            while(i<len(arr1) and j< len(arr2) and arr1[i]==arr2[j]):
                maxsum=maxsum+arr1[i]
                i=i+1
                j=j+1
        #print(i,j,s1,s2,maxsum,'loop')
    s1=0
    s2=0
    #print(c[0],c[1])
    i=c[0]+1
    j=c[1]+1
    while i< len(arr1):
        s1=s1+arr1[i]
        i=i+1
    while j< len(arr2):
        s2=s2+arr2[j]
        j=j+1
    #print(i,j,s1,s2,maxsum)
    maxsum=maxsum+max(s1,s2)
    return maxsum

def maxsum(arr1,arr2):
    flag=False
    for i in arr1:
        for j in arr2:
            if i==j:
                flag=True
                break
            if flag==True:
                break
    if flag==False:
        sum1,sum2=0,0
        for i in arr1:
            sum1=sum1+i
        for j in arr2:
            sum2=sum2+j
        return max(sum1,sum2)," old arrays"
    if flag==True:
        return treepath(arr1,arr2),"new arrays"


size1 = int(input())
n1= input()
n1 = n1.strip()
b1 = n1.split(" ")
for i in range(0, size1):
    b1[i] = int(b1[i])
size2 = int(input())
n2 = input()
n2 = n2.strip()
b2 = n2.split(" ")
for i in range(0, size2):
    b2[i] = int(b2[i])
b1.sort()
b2.sort()
#print(b1,b2)
print((maxsum(b1,b2))[0])