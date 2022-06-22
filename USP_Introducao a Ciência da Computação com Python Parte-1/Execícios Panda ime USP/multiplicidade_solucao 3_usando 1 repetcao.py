'''
Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos, indicando também a mutiplicidade de cada fator.

Por exemplo, para n = 600, a saída deverá ser:
fator 2 multiplicidade 3
fator 3 multiplicidade 1
fator 5 multiplicidade 2
'''



# Solução 3 usando apenas 1 repetição:

def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    mult = 0;

    while n != 1:
        # conta a multiplicidade de fator em n
        if n%fator == 0:
            n = n / fator;
            mult = mult + 1;
        else:
            # imprime a multiplicade do fator
            if mult != 0:
                print("fator %d multiplicidade %d" %(fator, mult))
                mult = 0

            fator = fator + 1

    # imprime a multiplicade do ultimo fator
    if mult != 0:
        print("fator %d multiplicidade %d" %(fator, mult))

main() # chamada da função principal