
MAX_CHAR = 26

def printCommon(s1, s2):
    a1 = [0 for i in range(MAX_CHAR)]
    a2 = [0 for i in range(MAX_CHAR)]

    length1 = len(s1)
    length2 = len(s2)

    for i in range(0, length1):
        a1[ord(s1[i]) - ord('a')] += 1

    for i in range(0, length2):
        a2[ord(s2[i]) - ord('a')] += 1
    flag=0
    flag1=0
    for i in range(0, MAX_CHAR):
        if (a1[i] != 0 and a2[i] != 0):
            flag1=1
            for j in range(0, min(a1[i], a2[i])):
                ch = chr(ord('a') + i)
                print(ch, end='')
        if (a1[i]==0 and a2[i]==0):
            flag=0
    if flag==0 and flag1==0:
        print(-1)

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    printCommon(s1, s2);
