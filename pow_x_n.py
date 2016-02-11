def powX_N(x,n):
    if n ==1:
        return x
    else:
        return x + powX_N(x, n - 1)
print(pow(2,6))