
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


n = 0
array = []

while len(array) < 100:
    array = [int(x) for x in str(fib_iteration_buffer(n))]
    n += 1

array = [int(x) for x in str(fib_iteration_buffer(n-2))]

print("MAX 99 CHAR FIBINACCI")
print(array)
print(''.join(map(str, array)))
print("n value: ", n-2)
print("length of array: ", len(array))














