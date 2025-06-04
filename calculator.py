#!/usr/bin/env python3

import argparse
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculate(a, b, op):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {op}")
    if op == '/' and b == 0:
        raise ZeroDivisionError('Division by zero')
    return OPERATIONS[op](a, b)


def main():
    parser = argparse.ArgumentParser(description='Simple command-line calculator')
    parser.add_argument('a', type=float, help='First operand')
    parser.add_argument('op', choices=OPERATIONS.keys(), help='Operation (+, -, *, /)')
    parser.add_argument('b', type=float, help='Second operand')
    args = parser.parse_args()

    result = calculate(args.a, args.b, args.op)
    print(result)


if __name__ == '__main__':
    main()
