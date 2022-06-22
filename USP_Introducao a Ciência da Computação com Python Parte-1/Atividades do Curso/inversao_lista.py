# inversão de lista
# impressão vertical


lista = []
x = int(input("Digite um número: "))
while x != 0:
    lista.append(x)
    x = int(input("Digite um número: "))
print()
for i in range(len(lista)-1,-1,-1):
    print(lista[i])