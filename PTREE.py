fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')

n, k = map(int,fi.readline().split())
h = list(map(int,fi.readline().split()))
h.sort()
count = 0

right = 0
for left in range(n):
    while right < n and h[right] - h[left] <= k:
        right += 1
    count += (right - left) - 1

fo.write(str(count))

fi.close()
fo.close()
