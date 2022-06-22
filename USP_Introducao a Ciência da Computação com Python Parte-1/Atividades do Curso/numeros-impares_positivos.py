    Programe que lê um inteiro positivo n e imprime os n 
    primeiros inteiros positivos.
    '''
    
    print("Gerador do n primeiros números ímpares positivos\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    # contador de ímpares impressos
    i = 0

    # imprima os n primeiros impares, um por linha
    while i < n: 
        # imprima o próximo ímpar
        print(2*i + 1)

        i = i + 1