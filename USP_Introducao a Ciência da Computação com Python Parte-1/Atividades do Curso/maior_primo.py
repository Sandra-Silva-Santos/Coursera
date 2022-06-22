def ehPrimo(k):
    divisores = 0
    for divisor in range(1, k):
        if k % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
            break
    if divisores > 1:
        return False
    else:
        return True

def maior_primo(x):
    primo = x
    i = 0
    while i <= x:
        if ehPrimo(i):
            primo = i
        i = i + 1
    return primo