'''
Title     : Exceptions
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/exceptions/problem
'''
n = int(input())
for i in range(n):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code: "+str(e))
