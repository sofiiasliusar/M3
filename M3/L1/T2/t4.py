'''
Давай намалюємо будинок! 
Яку площу він займе?

Користувач вводить чотири числа: 
a і b - сторони прямокутника, 
c і d - висота і основа трикутника.
Визначте функцію home_area, 
яка поверне площу будинку 
(тобто суму площ прямокутника і трикутника).

'''
def home_area(a, b, c, d):
    rectangular_area = a*b
    triangle_area = (c*d)/2
    total_area = rectangular_area + triangle_area
    return total_area

a = int(input("Введіть першу сторону прямокутника: "))
b = int(input("Введіть другу сторону прямокутника: "))
c = int(input("Введіть висоту трикутника: "))
d = int(input("Введіть основу трикутника: "))
print(home_area(a, b, c, d))
