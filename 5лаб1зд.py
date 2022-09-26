import math
x = int(input("Введіть x"))

def f1(a):
    return math.exp(3.27*abs(a-9)+1)

def f2(b):
    return math.cos(b)+ math.cos(b) / math.sin(b) + math.sqrt(abs(b - 7.84))

def f3(c):
    return math.sin(abs(c - 0.7)) + 3.33 * math.pow(2,c)
if x >= 5.2:
    print(f1(x))
elif x < 5.2 and x > 0.19:
    print(f2(x))
else:
    print(f3(x))