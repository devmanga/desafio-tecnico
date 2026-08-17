def true_primo(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True

def primos(b):
    if b <= 1:
        return []

    lista_primos = primos(b - 1)

    if true_primo(b):
        lista_primos.append(b)

    return lista_primos

b = int(input("Descubra os números primos até um determinado número: "))
print(f"Os números primos até {b} são: {primos(b)}")
