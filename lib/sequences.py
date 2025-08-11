def print_fibonacci(n):
    fib = [0, 1]  # Starting numbers of the Fibonacci sequence
    if n <= 0:
        print([])  # Print empty list for non-positive n
        return
    elif n == 1:
        print([0])
        return

    # Generate Fibonacci numbers up to length n
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]  # Sum of last two numbers
        fib.append(next_num)

    print(fib[:n])
print_fibonacci(9)
