l=[int(i) for i in input().split()]
s=sorted(L)
L=[]
for i in l:
    L.append(s.index(i))
print(L)
