import math
a= float(input("нижня межа"))
b = float(input("верхня межа"))
h = float(input("крок"))
a1 = a

s = []
s1 = []

for i in range(a,b+h,h):
    x = math.exp(a1)/a1**2+0.11
    a1 = round(a1,2)
    s.append(a1)
    s1.append(x)
    print("x = ",a1,"y=",x, "крок",i)
    a1+=h
    if a > b:
        break
print(s,s1)
