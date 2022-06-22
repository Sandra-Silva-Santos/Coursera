'''
Dada uma sequência de números inteiros maiores que um, terminada por um zero, determinar quantos números primos há na sequência.

Solução 2: Uso da função eh_primo
'''
def main():

    # leia um numero da sequencia
    num = int(input("Digite um numero (0 para terminar): "))

    cont = 0  # contador de primos
    while num != 0:
        if eh_primo(num):
            cont += 1

        num = int(input("Digite um numero (0 para terminar): "))

    print ("Achei %d primos na sequencia"%(cont))

#-----------------------------------------------------
def eh_primo(n):
    ''' (int) -> bool

    Recebe um numero inteiro positivo n e retorna True se n
    e' primo e False em caso contrario.
    '''
    primo = True
    i = 2
    while i <= n/2 and primo:
        if n % i == 0:    # se num eh multiplo de i
            primo = False   # num nao pode ser primo
        i += 1
    return primo

#-----------------------------------------------------
main()