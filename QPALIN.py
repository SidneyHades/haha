fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')




"""
#Cách 1
n, q = map(int,fi.readline().split())
s = fi.readline().strip()

def check(l, r):
    if l == 1:
        return s[l-1:r] == s[r-1::-1]
    else:
        return s[l-1:r] == s[r-1:l-2:-1]

for _ in range(q):
    l, r = map(int,fi.readline().split())
    if check(l, r):
        fo.write(str(1) + '\n')
    else:
        fo.write(str(0) + '\n')
"""

fi.close()
fo.close()
