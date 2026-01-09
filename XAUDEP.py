fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')

n = int(fi.readline())
s = fi.readline().strip()
count = 0

"""
#Cách 1
def check(s):
    return s[0] == s[-1] and (len(s) >= 2)

for i in range(n):
    for j in range(i+1, n+1):
        if check(s[i:j]):
            count += 1

fo.write(str(count))
"""

from collections import Counter

cnt = Counter(s)
kq = 0

for c in cnt.values():
    kq += c * (c - 1) // 2

fo.write(str(kq))

fi.close()
fo.close()
