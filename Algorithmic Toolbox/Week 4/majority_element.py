# Uses python3
import sys


def major_e(a, l, r):
    if (l == r):
        return a[l]
    mid = int((r - l) / 2) + l
    left = major_e(a, l, mid)
    right = major_e(a, mid + 1, r)

    if (left != None) and (right != None):
        if left == right:
            return left
    count_l = 0
    count_r = 0
    if (left != None):
        for i in range(l, r + 1):
            if a[i] == left:
                count_l = count_l + 1
    if (right != None):
        for i in range(l, r + 1):
            if a[i] == right:
                count_r = count_r + 1
    if (count_l > count_r) and (count_l > 0.5 * (r - l) + l):
        return left
    if (count_l < count_r) and (count_r > 0.5 * (r - l) + l):
        return right
    return None

def divide_func(seq, l, r):
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = divide_func(seq, l, m)
    right = divide_func(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    ele = divide_func(a, 0, n-1)
    if (ele != -1):
        print(1)
    else:
        print(0)

