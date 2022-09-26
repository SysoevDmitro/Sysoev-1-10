import math
a= float(input("нижня межа"))
b = float(input("верхня межа"))
h = float(input("крок"))
a1 = a

s = []
s1 = []

for i in range(10):
    x = math.exp(a1)/a1**2+0.11
    a1 = round(a1,2)
    s.append(a1)
    s1.append(x)
    a1+=h
    if a > b or a1 == b+h:
        break
print(s1)
print(s)
print(s1[:len(s1)//2])
print(s1[len(s1)//2:])