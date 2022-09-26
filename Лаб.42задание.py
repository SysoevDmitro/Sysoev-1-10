import math 
r = float(input())
q = int(input())
w = int(input())
e = int(input())
def func(a,y,z,x):
    return 6*a*x**3 + math.sin(y) + math.cos(z) + math.tan(x+math.pi/3)

print(func(q,w,e,r))