def get_recursion_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursion_factorial(n-1)

print(get_recursion_factorial(10))