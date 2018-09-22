
def fib_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursion(n-1) + fib_recursion(n-2)


# recursion
print("RECURSIVE")
print(fib_recursion(30))





