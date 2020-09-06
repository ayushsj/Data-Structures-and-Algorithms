# Uses python3
import sys


def pisano_period(m):
    curr, prev = 1, 0
    for i in range(2, m * m + 1):
        prev, curr = curr, (prev + curr) % m

        if (prev == 0) & (curr == 1):
            return i - 1

def calc_fib(n,m):
    f = list()
    for i in range(n+1):
        if i<2:
            f.append(i)
        else:
            f.append(f[i-1]+f[i-2])
    return f[n]%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    f = n%pisano_period(m)
    print(calc_fib(f, m))
