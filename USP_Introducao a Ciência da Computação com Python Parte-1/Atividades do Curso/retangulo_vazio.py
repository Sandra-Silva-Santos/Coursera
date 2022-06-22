largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
ALT = altura
LARG = largura
while altura > 0:
    x = 0
    while x < largura:
        if altura == (ALT) or x == (LARG - 1) or altura == 1 or x == 0:
            print("#" , end = '')
        else: 
            print(" " , end = '')
        x+=1
    altura = altura - 1
    print()