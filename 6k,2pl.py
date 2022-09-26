import math
a= float(input("нижня межа"))
b = float(input("верхня межа"))
h = float(input("крок"))
i=0
s = []
s1 = []
s2 = [s,s1]
while a!=b+h:
    x = math.exp(a)/a**2+0.11
    a = round(a,2)
    s.append(a)
    s1.append(x)
    print("x = ",a,"y=",x, "крок",i)
    a+=h
    if a > b:
        break
    i+=1
print(s2)
