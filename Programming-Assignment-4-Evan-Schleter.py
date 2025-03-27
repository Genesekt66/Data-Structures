def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def generate_fibonacci(n):
    for i in range(n):
        fib_list.append(fibonacci(i))

fib_list = []
fib_full = ""
x = int(input("To what number in the fibonacci sequence would you like to see?\n"))
generate_fibonacci(x)
print(f'Fibonacci at specified index: {fib_list[x-1]}')
for int in fib_list:
    fib_full += str(int) + " "
print(f'Full sequence: {fib_full}')