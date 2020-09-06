# python3

def brack_check(s):
    open_bracket = []
    open_index = []
    prob = -1
    counter = 0
    d = 'Success'
    for i in s:
        if (i=='{')or(i=='[')or(i=='('):
            c = open_bracket.append(i)
            f = open_index.append(counter)
        if (i=='}')or(i==']')or(i==')'):
            if len(open_bracket)==0:
                prob = counter
                break
            else:
                if (i=='}') and (open_bracket[-1]=='{'):
                    open_bracket.pop()
                    open_index.pop()
                elif (i==']') and (open_bracket[-1]=='['):
                    open_bracket.pop()
                    open_index.pop()
                elif (i==')') and (open_bracket[-1]=='('):
                    open_bracket.pop()
                    open_index.pop()
                else:
                    prob = counter
                    break
        counter = counter + 1
    if (prob == -1) and (len(open_bracket)==0):
        return d
    elif (prob == -1) and (len(open_bracket)!=0):
        return open_index[-1]+1
    else:
        return prob+1


def main():
    text = input()
    mismatch = brack_check(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
