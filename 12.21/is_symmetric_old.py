a = input() 
b = int(a[0]) # +8
d = int(a[1]) # +0
f = int(a[2]) # -4
k = int(a[3]) # -4
c = b - k + d - f + 1 
print(c) 

|
|
\/

a = input()
b = int(a[0] + a[1])
d = int(a[3] + a[2])

c = (b - d) + 1
print(c)