def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def print_to_n(n):
    if n == 0:
        return
    print_to_n(n - 1)
    print(n, end=' ')


def print_reverse(n):
    if n == 0:
        return
    print(n, end=' ')
    print_reverse(n - 1)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def to_binary(n):
    if n == 0:
        return ''
    return to_binary(n // 2) + str(n % 2)


def is_sorted(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)


def find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    max_rest = find_max(arr, index + 1)
    return arr[index] if arr[index] > max_rest else max_rest


def product_list(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_list(arr[1:])

