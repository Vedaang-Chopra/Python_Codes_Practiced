'''
def stringreverse(n):
    a=n.split(' ')
    #print(a)
    string=a.pop()
    for i in range(0,len(a)):
        string1=a.pop()
        string=string+" "
        string=string+string1

    return string
n=input()
print(stringreverse(n))
'''
