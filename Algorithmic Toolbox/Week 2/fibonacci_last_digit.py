# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    f = list()
    for i in range(n + 1):
        if i < 2:
            f.append(i)
        else:
            f.append(f[i - 1]%10 + f[i - 2]%10)
    return f[n]%10

n = int(input())
print(get_fibonacci_last_digit_naive(n))
