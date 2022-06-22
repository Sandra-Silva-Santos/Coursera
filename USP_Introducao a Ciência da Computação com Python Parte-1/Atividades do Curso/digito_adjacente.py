# Digito Adjacente


num = int(input("Digite um número e veja se ele é adjacente: "))
cond = True

while cond:
    x1 = num % 10
    x = num // 10
    x2 = x % 10
    if num <= 10:
        print('não')
        cond = False
    elif num > 10 and x1 == x2:
        print('sim')
        cond = False
    else:
        num = num // 10
        