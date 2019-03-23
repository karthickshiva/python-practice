'''
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all 
the elements to its right side. Also, the rightmost element is always a leader. 
'''
for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = [0]*n
    m[n-1] = a[n-1]
    
    for i in reversed(range(n-1)):
        m[i] = max(m[i+1], a[i])
    
    for i in range(n):
        if a[i] >= m[i]:
            print(a[i], end=" ")
    print()