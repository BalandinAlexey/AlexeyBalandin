second = int(input('Введите количество секунд: '))

d = 0
h = 0
m = 0

while second>86399:
    d += 1
    second -= 86400
while second>3599:
    h += 1
    second -= 3600
while second>59:
    m += 1
    second -= 60

if d<10:
    d = '0' + str(d)
if h<10:
    h = '0' + str(h)
if m<10:
    m = '0' + str(m)
if second<10:
    second = '0' + str(second)

print(d, ':', h, ':', m, ':', second)