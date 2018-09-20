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


def fib_iteration_hundred_digits(n):
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


#recursion
start = timer()
print(fib_recursion(10))
end = timer()

#iteration
start1 = timer()
print(fib_iteration(10))
end1 = timer()

# # for 100 digit array
# n = 35
# array = [int(x) for x in str(fib_iteration_hundred_digits(n))]
# print(array)
# print(len(array))

n = 10
array = []

while len(array) < 100:
    array = [int(x) for x in str(fib_iteration_hundred_digits(n))]
    n = n+1

print(array)
# timers
print((end - start))
print((end1 - start1))



