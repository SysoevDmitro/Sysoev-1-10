import random
a = int(input("Введите число строк"))
c = []
for i in range(a):
    b = input("Введите строку не больше 3 символов")
    c.append(b)
    if len(b) > 3:
        c.remove(b)
print
for x in c:
    print(x)
    y = list(x)
    random.shuffle(y)
    for v in y:
        print(v)
        
