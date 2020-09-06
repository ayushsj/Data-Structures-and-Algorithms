# Uses python3
def calc_fib(n):
    f = list()
    for i in range(n+1):
        if i<2:
            f.append(i)
        else:
            f.append(f[i-1]+f[i-2])
    return f[n]

n = int(input())
print(calc_fib(n))
