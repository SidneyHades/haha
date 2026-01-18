from collections import Counter
fi = open('CAU3.INP','r')
fo = open('CAU3.out','w')

n = int(fi.readline())
s = fi.readline().strip()
a = []
mx = 0

for i in range(n):
    for j in range(i+1,n+1):
        if len(s[i:j]) != 0:
            a.append(s[i:j])

count = Counter(a)

for ch, c in count.items():
    if c >= 2:
        mx = max(len(ch), mx)

fo.write(str(mx))
        
fi.close()
fo.close()
