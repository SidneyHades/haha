fi = open('TEST.INP','r')
fo = open('TEST.OUT','w')

#Cách 1
a, b = map(int,fi.readline().split())
count = 0

def special(x):
    tong = 1 + x
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            tong += i
            if x // i != i:
                tong += (x//i)
    return tong 

for i in range(a, b + 1):
    if special(i):
        count += 1

fo.write(str(count))


fi.close()
fo.close()
