import math
print("Титов Алексей Дмитриевич РРБО-02-20\n", 3 + 5)
x = int(input("Введите X\n"))
print(x ** 5 - 2 * x ** 3 - 1)
strange = [ [], 1]
print(type(strange))
mask = [1, 2, 3, 4]
print(mask[::-1])
n = int(input("Введи n\n"))
print(math.log2(n))
z = float(input("Введи z\n"))
print(math.tan(math.cos(z) * math.sin(2 * z) / z * math.exp(z)) ** math.log(z, 7))
sask = [0, 0, 1, 1, 1, 0, 1, 0]
if sask.count(1) % 2 == 0:
    sask.append(0)   
else:
    sask.append(1)
print (sask)