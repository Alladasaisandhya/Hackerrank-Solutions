'''
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
'''
import numpy
n,m = map(int,input().split())
print(numpy.eye(n,m,k=0))
