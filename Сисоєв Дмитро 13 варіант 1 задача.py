n1 = int(input("Введите целое число: "))
n2 = int(input("Введите целое число: "))
n3 = 0
n4 = 0

n3 = (n1%10) * 10 + n1 // 10
n4 = (n2%10) * 10 + n2 // 10
 
print('"Обратное" им числа:', n3, n4)