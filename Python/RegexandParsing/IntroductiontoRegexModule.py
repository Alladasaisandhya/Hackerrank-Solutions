'''
Title     : Introduction to Regex Module
Subdomain : Regex and Parsing
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/introduction-to-regex/problem
'''
import re
n = int(input())
for i in range(n):
    s = input()    
    search_result = re.search(r'^[+-]?\d*\.\d+$',s)
    print(bool(search_result))
