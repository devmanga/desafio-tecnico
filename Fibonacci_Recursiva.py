def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Descubra um número na sequência Fibonacci: "))
print(f"O número correspondente à esse número na sequência Fibonacci é fib({n}) = {fibonacci(n):,}".replace(',', '.'))
