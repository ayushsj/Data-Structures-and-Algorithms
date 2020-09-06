# Uses python3
import sys

def change(money):
    coins = [1,3,4]
    cmin = [None]*(money+1)
    cmin[0]=0
    for m in range(1,money+1):
        for i in coins:
            if m>= i:
                numc = cmin[m-i]+1
                if cmin[m] == None:
                    cmin[m] = numc
                if cmin[m]>numc:
                    cmin[m] = numc
    return cmin[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(change(m))
