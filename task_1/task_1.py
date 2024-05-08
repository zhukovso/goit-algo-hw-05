def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n < 0:
            raise ValueError
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n] 
    return fibonacci


def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
    print(fib(6))   # Виведе 8


if __name__ == '__main__':
    main()
