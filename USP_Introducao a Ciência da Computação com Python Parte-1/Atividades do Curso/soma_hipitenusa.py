# soma_hipotenusa

def é_hipotenusa(a, b):
    hipotenusa = ((a*a) + (b*b))
    return hipotenusa


def soma_hipotenusas(h):
    c = 1
    soma = 0
    while (c <= h):
        c2 = (c**2)
        a = 1
        b = 1
        while (a < h):
            while (b < h):
                if (c2 == é_hipotenusa(a, b)):
                    soma += c
                    a = h
                    break
                b += 1
            a += 1
            b = a
        c += 1
    return soma


def iniciar():
    x = int(input("Digite um número inteiro e positivo: "))
    while x < 1:
        print("Número inválido! Tente novamente.")
        print()
        x = int(input("Digite um número inteiro e positivo: "))
    print(soma_hipotenusas(x))



if __name__ == "__main__":
    iniciar()