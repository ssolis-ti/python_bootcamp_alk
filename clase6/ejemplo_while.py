numero = 5
while numero >=3:
    # print(numero)
    # numero = numero - 1
    numero -= 1


#break y continue

for numero in range(1000000000):
    print(numero)
    if numero == 3:
        break
print("ejmplo continue")

for numero in range(10):
    if numero == 3:
        print("ingresamos al continue")
        continue
    print(numero) 