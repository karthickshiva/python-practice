'''
Given an array A of N positive integers. Find the sum of maximum sum increasing subsequence of the given array.
'''
for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    MSIS = list(a)
    
    for i in range(1, len(a)):
        for j in range(0, i):
            if(a[j] < a[i]):
                MSIS[i] = max(MSIS[i], MSIS[j] + a[i])
    print(max(MSIS))