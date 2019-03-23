'''
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
'''

a = [6, 5, 1, 2, 3]
n = len(a)+1
print ((n*(n+1))/2) - sum(a)