# python3
import sys


def num_ref(d,m,stops):
    x = list()
    x.append(0)
   # print('x',x)
    for i in stops:
        x.append(i)
   # print('x',x)
    x.append(d)
   # print('x',x)
    r_num = 0
    curr_p = 0
    n = len(stops)
    #print('n',n)
    while curr_p<=n:
        last_p = curr_p
      #  print('last',last_p)
     #   print('curr',curr_p)
       # print('ref',r_num)
        while(curr_p<=n)and(x[curr_p+1]-x[last_p]<=m):
            curr_p = curr_p+1
        #    print('curr',curr_p)
        if (curr_p==last_p):
            return -1
        if (curr_p<=n):
            r_num = r_num + 1
         #   print('ref',r_num)
    return r_num

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(num_ref(d, m, stops))

