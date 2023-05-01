#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:57:49 2023

@author: chinmayakumarpalo
"""

import math

print("Scientific Calculator")

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Square")
    print("6.Square Root")
    print("7.Logarithm")
    print("8.Sin")
    print("9.Cos")
    print("10.Tan")
    print("11.Cosec")
    print("12.Sec")
    print("13.Cot")
    print("14.Quit")

    choice = input("Enter choice (1-14): ")

    if choice == '14':
        break

    num1 = float(input("Enter first number: "))

    if choice == '5' or choice == '6':
        pass
    else:
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2,"\n")

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2,"\n")

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2,"\n")

    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1, "/", num2, "=", num1 / num2,"\n")

    elif choice == '5':
        print(num1, "^2 =", num1 ** 2,"\n")

    elif choice == '6':
        print("√", num1, "=", math.sqrt(num1),"\n")

    elif choice == '7':
        print("log", num1, "=", math.log10(num1),"\n")

    elif choice == '8':
        print("sin", num1, "=", math.sin(num1),"\n")

    elif choice == '9':
        print("cos", num1, "=", math.cos(num1),"\n")

    elif choice == '10':
        print("tan", num1, "=", math.tan(num1),"\n")

    elif choice == '11':
        print("cosec", num1, "=", 1/math.sin(num1),"\n")

    elif choice == '12':
        print("sec", num1, "=", 1/math.cos(num1),"\n")

    elif choice == '13':
        print("cot", num1, "=", 1/math.tan(num1),"\n")

    else:
        print("Invalid input","\n")
