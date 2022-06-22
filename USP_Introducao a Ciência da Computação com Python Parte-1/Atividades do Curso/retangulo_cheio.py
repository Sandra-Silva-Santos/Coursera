largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
while altura > 0:
    x = 0
    while x < largura:
        print("#" , end = '') 
        x+=1
    altura = altura - 1
    print()