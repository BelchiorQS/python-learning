import random

num_i = 10
num_f = 5.2
num_c = 1j
num_r = [random.randrange(0, 59), random.randrange(0, 59), random.randrange(0, 59), random.randrange(0, 59), random.randrange(0, 59), ]

x = num_i

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
print("Valor 1 : " + str(num_r[0]))
print("Valor 2 : " + str(num_r[1]))
print("Valor 3 : " + str(num_r[2]))
print("Valor 4 : " + str(num_r[3]))
print("Valor 5 : " + str(num_r[4]))