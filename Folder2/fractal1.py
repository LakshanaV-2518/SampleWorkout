def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Number of terms in the Fibonacci series
n = 10

# Print the Fibonacci series
fibonacci(n)
