'''
Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.

Por exemplo, para n = 6, i = 2 e j = 3 a saída deverá ser:
0   2   3   4   6   8
'''


# Solução


def main():
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))

    # mutiplos de i e j
    mult_i = mult_j = 0

    k = 0
    while k < n:
        if mult_i == mult_j:
            print(mult_i)
            mult_i = mult_i + i
            mult_j = mult_j + j
        elif mult_i < mult_j:
            print(mult_i)
            mult_i = mult_i + i
        else:
            print(mult_j)
            mult_j = mult_j + j;

        k = k + 1


main()