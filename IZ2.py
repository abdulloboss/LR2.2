x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

# Вычисляем максимум и минимум с использованием условных операторов
u1 = x**2 * y
u2 = x * y**2

if u1 > u2:
    max_u = u1
else:
    max_u = u2

min1 = x - y
min2 = x + 2 * y

if min1 < min2:
    min_u = min1
else:
    min_u = min2

# Выводим результаты
print(f"U = max^2(x^2*y, x*y^2) = {max_u}")
print(f"V = min^2(x-y, x+2*y) = {min_u}")