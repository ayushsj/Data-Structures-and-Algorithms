# Uses python3
import sys

def prize(n):
    l = []
    left = n
    for i in range(1,n+1):
        if left-i>i:
            l.append(i)
            left = left - i
        else:
            l.append(left)
            return l

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = prize(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
