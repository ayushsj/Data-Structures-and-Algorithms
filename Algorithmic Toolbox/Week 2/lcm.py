# Uses python3
import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int((a*b)/gcd(a, b)))

