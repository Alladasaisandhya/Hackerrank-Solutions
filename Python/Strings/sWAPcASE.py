'''
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
'''

def swap_case(s):
    newstring = ""
    
    for item in s:
        if item.isupper():
            newstring += item.lower()
        else:
            newstring += item.upper()
            
    return newstring
