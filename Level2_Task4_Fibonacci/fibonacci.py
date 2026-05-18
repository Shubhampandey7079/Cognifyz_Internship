def fibonacci(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result


num = int(input("Enter number of terms: "))

if num <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Sequence:")
    print(fibonacci(num))