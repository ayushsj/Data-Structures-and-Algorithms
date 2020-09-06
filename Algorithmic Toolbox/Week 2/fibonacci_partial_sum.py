# Uses python3
import sys

def sum_f(m,n):
    x = 60
    num_n = n%x
    num_m = (m-1)%x
    prev_n,curr_n = 0,1
    prev_m,curr_m = 0,1
    if num_n<2:
        curr_n = num_n
    else:
        for i in range(2,num_n+1):
            prev_n,curr_n = curr_n, (curr_n+prev_n+1)%10
    if num_m<2:
        curr_m = num_m
    else:
        for i in range(2,num_m+1):
            prev_m,curr_m = curr_m, (curr_m+prev_m+1)%10
    if curr_n - curr_m>=0:
        return curr_n - curr_m
    else:
        return 10 - curr_m + curr_n


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(sum_f(from_, to))