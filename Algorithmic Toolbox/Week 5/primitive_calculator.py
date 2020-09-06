# Uses python3
import sys

def sequence(n):
    seq = []
    seq.append([0,0])
    seq.append([0,1])
    for i in range(1,n+1):
        if i%2==0:
            op = [seq[int(i/2)][0]+1,int(i/2)]
            if len(seq)==i:
                seq.append(op)
            elif len(seq)==i+1:
                if seq[i][0]>seq[int(i/2)][0]+1:
                    seq.pop()
                    seq.append(op)
        if i%3==0:
            op = [seq[int(i/3)][0]+1,int(i/3)]
            if len(seq)==i:
                seq.append(op)
            elif len(seq)==i+1:
                if seq[i][0]>seq[int(i/3)][0]+1:
                    seq.pop()
                    seq.append(op)
        if True:
            op = [seq[i-1][0]+1,i-1]
            if len(seq)==i:
                seq.append(op)
            elif len(seq)==i+1:
                if seq[i][0]>seq[i-1][0]+1:
                    seq.pop()
                    seq.append(op)
    l = []
    num = n
    while True:
        if num == 1:
            l.append(num)
            break
        l.append(num)
        num = seq[num][1]
    return reversed(l)

input = sys.stdin.read()
n = int(input)
sequence = list(sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
