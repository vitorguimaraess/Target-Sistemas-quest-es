def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

print(verifica_fibonacci(int(input()))) 