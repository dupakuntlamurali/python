def calculate(self,s):
    s=s.replace(" ", "")
    pn=[1 if c=="+" else -1 for c in s if c in "+-"]
    sList=[self.cal(c) for c in s.replace("-", "+").split("+")]

    return sList[0]+sum([sList[i+1]*pn[i] for i in xrange(len(pn))])
def cal(self,s):
    if "x" not in s and "/" not in s:
        return int(s)
