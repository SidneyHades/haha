fi = open('CAU2.INP','r')
fo = open('CAU2.out','w')

l, r, k = map(int,fi.readline().split())

def sieve(n):
    a = [True]*(n+1)
    a[0] = a[1] = False

    for i in range(2, int(n**0.5) + 1):
        if a[i]:
            a[i*i:n+1:i] = [False]*len(range(i*i, n+1, i))
    return a

day = sieve(r)
count = 0

for i in range(l, r+1):
    if day[i]:
        s = sum(int(c) for c in str(i))
        if s % k == 0:
            count += 1

fo.write(str(count))
        
fi.close()
fo.close()
