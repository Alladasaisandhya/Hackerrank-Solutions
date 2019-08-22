'''
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input()
in_str_ar=raw_input().strip().split()
pos=int(in_str_ar[0])
c=in_str_ar[1]
final_str=s[:pos]+c+s[pos+1:]
print final_str
