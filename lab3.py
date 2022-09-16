## Четвртий варіант,перше завдання
a = int(input("please enter a(1-9):"))
b = int(input("please enter b(0-9)"))
c = int(input("please enter c(0-9)"))
d = int(input("please enter d(0-9)"))
e = a*1000+b*100+c*10+d
suma = a+b+c+d
print(f"{e} - ваше чотирицифрове число.")
print(f"Сума цифр: {suma}")