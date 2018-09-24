def fib_iteration(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    minus_two = 0
    minus_one = 1

    for x in range(1, n):
        result = minus_two + minus_one
        minus_two = minus_one
        minus_one = result

    return result


# iteration
print("ITERATIVE")
print(fib_iteration(10))
print(fib_iteration(20))
print(fib_iteration(30))
