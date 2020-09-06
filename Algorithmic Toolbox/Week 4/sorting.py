# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def partition(a,l,r):
    j = l-1
    k = l
    p = a[l]
    for i in range(l+1,r+1):
        if a[i]<p:
            a[j+1],a[i]=a[i],a[j+1]
            j = j+1
            a[i],a[k+1]=a[k+1],a[i]
            k=k+1
        if a[i]==p:
            a[i],a[k+1]=a[k+1],a[i]
            k=k+1
    return j,k


def improv_qs(a, l, r):
    if l >= r:
        return
    j, k = partition(a, l, r)

    improv_qs(a, l, j);
    improv_qs(a, k + 1, r);
    return


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    improv_qs(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
