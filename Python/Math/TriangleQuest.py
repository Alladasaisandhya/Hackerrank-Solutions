'''
Title     : Triangle Quest
Subdomain : Math
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/python-quest-1/problem
'''
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*((pow(10,i)-1)/(9))
