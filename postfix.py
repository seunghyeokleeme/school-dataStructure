from listStack import *

def evaluate(p):
    s = ListStack()
    digitPreviously = False
    for i in range(len(p)):
        ch = p[i]
        if ch.isdigit():
            if digitPreviously:
                tmp = s.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                s.push(tmp)
            else:
                s.push(ord(ch) - ord('0'))
                digitPreviously = True
        elif isOperator(ch):
            s.push(operation(s.pop(), s.pop(), ch))
            digitPreviously = False
        else:
            digitPreviously = False
    return s.pop()

def isOperator(ch) -> bool:
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2: int, opr1: int, ch) -> int:
    return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}[ch]

def main():
    postfix = "700 3 47 + 6 * - 4 /"
    print("Input String: ", postfix)
    answer = evaluate(postfix)
    print("Answer: ", answer)
    print(ord('0'), ord('9'))

if __name__ == "__main__":
    main()