fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')

a, b = map(int,fi.readline().split())

tong = (pow(a, b, 100) + pow(b, a, 100)) % 100
fo.write(f"{tong:02d}")

fi.close()
fo.close()
