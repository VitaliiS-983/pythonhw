def charFreq(n):
    c={}
    for i in (range(len(n))):
        if (n[i] in c):
            c[n[i]]=int(c.get(n[i]))+1
        else:
            c[n[i]]=1     
    return c
nt=input("Enter any String:")
n=charFreq(nt)

print(n)
