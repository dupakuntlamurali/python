def roman(s):
    romand={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    i=0
    while i<len(s):
        if i+1<len(s) and romand[s[i]]<romand[s[i+1]]:
            total+=romand[s[i+1]]-romand[s[i]]
            i+=2
        else:
            total+=romand[s[i]]
            i+=1
    return total
print(roman('III'))
print(roman('LVIII'))
print(roman('MCMXCIV'))
print(roman('LV'))
