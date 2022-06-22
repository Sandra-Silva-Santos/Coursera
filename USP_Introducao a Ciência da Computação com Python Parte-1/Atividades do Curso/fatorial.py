# Fatorial
# Para recordar
# Exemplo: Fatirial 4 = 5x4x3x2x1 = 120


n = int(input("Digite o valor de n: "))


fatorial = 1

while n > 0:
    fatorial = fatorial * n
    n = n - 1
#   n -=1 também pode ser escrito desta forma
print(fatorial)