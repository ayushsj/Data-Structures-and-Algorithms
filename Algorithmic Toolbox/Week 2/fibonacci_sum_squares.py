# Uses python3
from sys import stdin

def f_last(n):
    prev, curr = 0,1
 #   num = n%60
    if n<2:
        return n
    else:
        for i in range(2,n+1):
            prev,curr = curr%10,(curr +prev)%10
    return curr
def f_sq(n):
    return (f_last(n % 60)*f_last((n+1) % 60))%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(f_sq(n))
