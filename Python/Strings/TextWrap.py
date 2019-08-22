'''
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
'''
import textwrap
s = input()
w = int(input().strip())
print(textwrap.fill(s,w))
