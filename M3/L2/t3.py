'''
Потрібно порахувати добуток чисел від a до b. 
Програма запитує числа і виводить результат.
Програма запитує у людини спочатку перше число, потім друге. 
Після цього програма повинна перемножити всі числа від a до b 
(припускаючи, що a < b) і надрукувати результат. 
Приклад: Введено числа 5 і 7. 
Програма надрукує "210" (5 * 6 * 7 = 210).
'''
print("Введіть 2 числа a < b:")
a = int(input("Число а:"))
b = int(input("Число b:"))

def func(a, b):
    result = 1
    for i in range(a, b + 1):
        result *= i
    return result

print(func(a, b))
