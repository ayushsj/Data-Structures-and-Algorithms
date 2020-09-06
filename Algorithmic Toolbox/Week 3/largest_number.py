#Uses python3

import sys

def iGoE(c,d):
    if c+d > d+c:
        return True
    else:
        return False

def salary(a):
    res = ''
    while len(a)>0:
        maxDigit = '0'
        for x in a:
            if iGoE(x,maxDigit):
                maxDigit = x
        res = res + maxDigit
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(salary(a))
    
