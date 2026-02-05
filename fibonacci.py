def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
terms = int(input("Number of terms: "))
print([fib(i) for i in range(terms)])
