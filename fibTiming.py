from timeit import default_timer as timer


def fib_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursion(n-1) + fib_recursion(n-2)


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


def fib_iteration_buffer(n):
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

# recursion
print("RECURSIVE")
start = timer()
fib_recursion(35)
end = timer()
print ("    time:",(end - start))

# iteration
print("ITERATIVE")
start1 = timer()
fib_iteration(35)
end1 = timer()
print ("    time:",(end1 - start1))