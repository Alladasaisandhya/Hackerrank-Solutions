'''
Title     : Sort Data
Subdomain : Built-Ins
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/python-sort-sort/problem
'''
n, m = map(int,input().split())
ar = []
for i in range(n):
    ar.append(list(map(int,input().split())))
k = int(input())
ar = sorted(ar,key = lambda x:x[k])
for i in ar:
    [print(x,end=' ') for x in i]
    print('')
