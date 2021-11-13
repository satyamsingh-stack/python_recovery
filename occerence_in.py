from collections import Counter
a=input().split()
b=Counter(a)
b=dict(b)
c=list(b.keys())
d=list(b.values())
print(c)
print(d)
print(c[d.index(max(d))])