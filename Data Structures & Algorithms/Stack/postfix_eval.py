# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:02:42 2020

@author: CHINMAY
"""

import operator as op


def Solve(Postfix):
    Stack = []
    Div = lambda x, y: int(x / y)  # noqa: E731 integer division operation
    Opr = {
        "^": op.pow,
        "*": op.mul,
        "/": Div,
        "+": op.add,
        "-": op.sub,
    }  # operators & their respective operation

    # print table header
    print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
    print("-" * (30 + len(Postfix)))

    for x in Postfix:
        if x.isdigit():  # if x in digit
            Stack.append(x)  # append x to stack
            # output in tabular format
            print(x.rjust(8), ("push(" + x + ")").ljust(12), ",".join(Stack), sep=" | ")
        else:
            B = Stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + B + ")").ljust(12), ",".join(Stack), sep=" | ")

            A = Stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + A + ")").ljust(12), ",".join(Stack), sep=" | ")

            Stack.append(
                str(Opr[x](int(A), int(B)))
            )  # evaluate the 2 values popped from stack & push result to stack
            # output in tabular format
            print(
                x.rjust(8),
                ("push(" + A + x + B + ")").ljust(12),
                ",".join(Stack),
                sep=" | ",
            )

    return int(Stack[0])


if __name__ == "__main__":
    Postfix = input("\n\nEnter a Postfix Equation (space separated) = ").split(" ")
    print("\n\tResult = ", Solve(Postfix))