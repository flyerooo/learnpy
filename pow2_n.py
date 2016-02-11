def factorial(n):
    if n == 1:
        return 2
    else:
        return 2 * factorial(n - 1)

print(factorial(5))