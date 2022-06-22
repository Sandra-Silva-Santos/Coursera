def main():
    '''
    Programa que lê um número inteiro x e um número inteiro n maior ou igual 
    a zero e imprime x elevado a n.

    Este programa está errado.
    '''

    print("Cálculo de potências\n")

    # leia a base
    x = int(input("Digite a base (número inteiro): "))

    # leia o expoente
    n = int(input("Digite o expoente (inteiro >= 0): "))

    # expoente
    i  = 0

    # calcule x elevado a n
    while i < n:
        i = i + 1 
        x = x * x # ERRO: precisamos de uma variável para as potências

    print("O valor de", x, "elevado a", n, "é", x) 