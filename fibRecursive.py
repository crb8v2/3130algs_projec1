from timeit import default_timer as timer

start = timer()


def fib_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursion(n-1) + fib_recursion(n-2)


end = timer()
start1 = timer()


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


end1 = timer()

print(fib_recursion(6))


print(fib_iteration(6))


print((end - start)*10000000)

print((end1 - start1)*10000000)



