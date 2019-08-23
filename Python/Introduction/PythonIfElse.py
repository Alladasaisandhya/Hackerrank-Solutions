'''
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
'''
#!/bin/python3

import sys


N = int(input().strip())
n= N
w = 'Weird'
nw = 'Not Weird'
if n % 2 == 1:
    print(w)
elif n % 2 == 0 and (n>=2 and n<5):
    print(nw)
elif n % 2 == 0 and (n>=6 and n<=20):
    print(w)
elif n % 2 == 0 and (n>20):
    print(nw)    
