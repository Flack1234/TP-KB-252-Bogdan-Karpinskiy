def disc(a, b, c):
    return b ** 2 - 4 * a * c
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))
print("Дискримінант дорівнює:", disc(a, b, c))