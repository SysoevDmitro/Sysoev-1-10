a = input("Введите символы")
b= 0
c = 1
print(a)
for i in a:
    if i.isdigit() == True:
        b+=int(i)
        c*=int(i)

print(b)
print(c)