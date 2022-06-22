# Numero Primo

numero = int(input("Digite um numero inteiro e veja se é primo: "))
i = numero - 1

while i > 0:
    if i == 1:
        print('primo')
        break
    elif (numero % i == 0):
        print('não primo')
        break
    else:
        i -= 1
        