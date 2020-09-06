# Uses python3
import sys

def get_change(m):
    a = 0
    coin = m
    for i in [10,5,1]:
        a = a + int(coin/i)
        coin = coin%i
    return a

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
