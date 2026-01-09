fi = open('TAMGIAC.INP','r')
fo = open('TAMGIAC.OUT','w')

a = []
for _ in range(4):
    x, y = map(float,fi.readline().split())
    a.append((x,y))

def stamgiac(a, b, c):
    def vecto(p, q):
        return (q[0] - p[0], q[1] - p[1])

    def tichcohuong(u, v):
        return u[0]*v[1] - u[1]*v[0]

    ab = vecto(a, b)
    ac = vecto(a, c)
    return abs(tichcohuong(ab, ac)) / 2

sabc = stamgiac(a[0],a[1],a[2])
ssum = (
    stamgiac(a[3], a[0], a[1]) +
    stamgiac(a[3], a[1], a[2]) +
    stamgiac(a[3], a[2], a[0])
)

eps = 10**-9

if (ssum-sabc) < eps:
    fo.write(str('1'))
else:
    fo.write(str('0'))


fi.close()
fo.close()
