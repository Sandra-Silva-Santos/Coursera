'''
Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos, indicando também a mutiplicidade de cada fator.

Por exemplo, para n = 600, a saída deverá ser:
fator 2 multiplicidade 3
fator 3 multiplicidade 1
fator 5 multiplicidade 2
'''



# Solução 2 utilizando função fatoracao que retorna 2 valores:

def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    while n != 1:
        # conta a multiplicidade de fator em n
        n, mult = fatora(n, fator)

        # imprime a multiplicade do fator
        if mult != 0:
            print("fator %d multiplicidade %d" %(fator, mult))

        fator = fator + 1

# --------------------------------------------------
def fatora(n, f):
    ''' (int, int) -> int, int
        fatora n por f. Retorna o novo valor de n e
        a multiplicidade de f.
    '''
    mult = 0
    while n%f == 0:
       n = n / f
       mult = mult + 1
    return n, mult

# --------------------------------------------------
main() # chamada da função principal