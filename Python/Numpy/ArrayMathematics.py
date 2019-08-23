'''
Title     : Array Mathematics
Subdomain : Numpy
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/np-array-mathematics/problem
'''
import numpy
n,m = map(int,input().split())
ar1 = []
ar2 = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ar1.append(tmp)
for i in range(n):
    tmp = list(map(int,input().split()))
    ar2.append(tmp)
np_ar1 = numpy.array(ar1)
np_ar2 = numpy.array(ar2)
print(np_ar1 + np_ar2)
print(np_ar1 - np_ar2)
print(np_ar1 * np_ar2)
print(np_ar1 // np_ar2)
print(np_ar1 % np_ar2)
print(np_ar1 ** np_ar2)
