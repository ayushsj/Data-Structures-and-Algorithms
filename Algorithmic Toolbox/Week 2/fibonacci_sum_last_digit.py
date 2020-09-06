# Uses python3
import sys

def sum_f(n):
    m = 60
    num = n%m
    prev,curr = 0,1
    if num<2:
        return num
    else:
        for i in range(2,num+1):
            prev,curr = curr, (curr+prev+1)%10
    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(sum_f(n))
