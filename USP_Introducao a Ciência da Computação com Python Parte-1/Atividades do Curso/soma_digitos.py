x = int(input("Digite um número para que seus dígitos sejam somados: "))

soma = 0
while x > 0:
    resto = x % 10
    x = x // 10
    soma = soma + resto

print(soma)