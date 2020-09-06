# python3


def max_product_fast(n,numbers):
    max2 = 0
    max1 = 0
    c1 = 0
    counter = 0
    for i in numbers:
        if i>=max1:
            max1 = i
            c1 = counter
        counter = counter + 1
        
    counter = 0
    for i in numbers:
        if (i >= max2)&(counter != c1):
            max2 = i
        counter = counter + 1
    return int(max1*max2)
    
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [float(x) for x in input().split()]
    print(max_product_fast(input_n,input_numbers))
