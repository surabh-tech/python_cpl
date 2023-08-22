def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

# Get input from the user
n = int(input("Enter the value of n: "))

# Call the function to generate and print Fibonacci series
result = fibonacci_series(n)
print("Fibonacci Series up to", n, "numbers:", result)
