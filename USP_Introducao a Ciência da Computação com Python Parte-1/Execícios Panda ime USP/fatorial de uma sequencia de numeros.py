'''
Dados um número inteiro n, n > 0, e uma sequência com n números inteiros maiores do que zero, determinar o fatorial de cada número da sequência.
'''

# Solução


def main():

    # leia o tamanho da sequencia
    n = int(input("Digite o tamanho da sequencia (>0): "))

    i = 0 # contador de numeros lidos
    while i < n:
        num = int(input("Digite o %do. numero: " %(i+1)))
        i = i + 1
        print ("%d ! = %d" %(num,fatorial(num)))

#-----------------------------------------------------
def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k e' um numero inteiro nao negativo.
    '''

    k_fat = 1
    i = 2
    while i <= k:
        k_fat *= i
        i += 1

    return k_fat

#-----------------------------------------------------
main()