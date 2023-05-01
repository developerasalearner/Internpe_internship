#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:29:12 2023

@author: chinmayakumarpalo
"""
def inpu ():
    def sum (a,b):
        return(a+b)

    def sub (a,b):
        return(a-b)

    def mul (a,b):
        return(a*b)

    def div (a,b):
        return(a/b)

    def mod (a,b):
        return(a%b)
    a=int(input('Enter the 1st number: '))
    b=int(input('Enter the second number: '))
    x=0   
    while x!=7:
        print("press 1 for addition")
        print("press 2 for dividion")
        print("press 3 for multiplication")
        print("press 4 for division")
        print("press 5 for modulous")
        print("press 6 for restarting the calculator")
        print("press 7 for exit")
        x=int(input())
        if x==1:
            print("Sum is: ",sum(a,b))
        elif x==2:
            print("Substration is is: ", sub(a,b))
        elif x==3:
            print("Multiplication is: ", mul(a,b))
        elif x==4:
            print("Division is: ", div(a,b))
        elif x==5:
            print("Modulos is: ", mod(a,b))
        elif x==6:
            inpu()
        elif x==7:
            print("EXited")
            break
            return
        else:
            print("Enter the correct input")
            inpu()
inpu()
