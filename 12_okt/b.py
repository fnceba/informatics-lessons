a = int(input())
b = int(input())
c = int(input())
if a<10:
    a='0'+str(a)
if b<10:
    b=f'0{b}'
if c<10:
    c='0{}'.format(c)

print(f"{a}:{b}:{c}")