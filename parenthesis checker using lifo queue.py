import queue

q = queue.LifoQueue(maxsize=10)


def bracket_check():
    exp = input("Enter the expression:")
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            q.put(i)
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            if q.qsize() == 0:
                return False
            temp = q.get()
            if exp[i] == ')' and (temp == '{' or temp == '['):
                return False
            elif exp[i] == '}' and (temp == '(' or temp == '['):
                return False
            elif exp[i] == ']' and (temp == '{' or temp == '('):
                return False

    if q.qsize() != 0:
        return False
    return True


def main():
    a = bracket_check()
    if a:
        print('Valid expression')
    else:
        print("Invalid expression")
    a = input("want to continue(y/n):")
    if a.lower() == 'y':
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
