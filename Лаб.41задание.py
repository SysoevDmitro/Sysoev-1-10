import math 
x=int(input("Введіть x "))
a = 2.7 * math.log1p(abs(math.sin(math.sqrt(x))))
b = abs(math.sqrt(x)+x*1/3) + 0.02
print(a- 8/b)