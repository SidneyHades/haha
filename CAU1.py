fi = open('CAU1.INP','r')
fo = open('CAU1.OUT','w')

a = list(map(int,fi.readline().split()))

tang = sorted(a)
giam = sorted(a, reverse=True)

if a == giam:
    fo.write(str('descending'))
elif a == tang:
    fo.write(str('ascending'))
else:
    fo.write(str('mixed'))

fi.close()
fo.close()
