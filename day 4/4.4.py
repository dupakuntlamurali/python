s=input()
s=s.lower()
d=""
for i in s:
    if(i==" " or i=="." or i=="," or i==":"):
        continue
    else:
        d=d+i
st=""
for i in s:
    if(i==" " or i=="." or i=="," or i==":"):
        continue
    else:
        st=st+i

if(d==st[::-1]):
    print("true")
else:
    print("false")
