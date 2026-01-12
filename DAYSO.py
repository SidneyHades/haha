fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')

n = int(fi.readline())
b = list(map(int,fi.readline().split()))
a = [0]*n
a[0] = b[0]

for i in range(1,n):
    a[i] = (i+1)*(b[i]) - i*b[i-1]

for x in a:
    fo.write(str(x) + " ")

fi.close()
fo.close()
