# Uses python3
import sys

def opt_v(c,w,v):
    tot_val = 0
    l = list()
    for i in range(len(w)):
        l.append((v[i]/w[i],w[i]))
    l = sorted(l,reverse=True)
    for i in l:
        #print(i, c)
        if c==0:
            return tot_val
        else:
            if c>i[1]:
                tot_val = tot_val + i[1]*i[0]
                c = c-i[1]
                #print('tv:',tot_val)
                #print('c:',c)
            else:
                tot_val = tot_val + (c)*i[0]
                #print('tv:',tot_val)
                #print('c:',c)
                c = 0
    return tot_val

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = opt_v(capacity, weights, values)
    print("{:.10f}".format(opt_value))
