'''
Given a sequence A of size N, find the length of the longest increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence of a given sequence 
in which the subsequence's elements are in sorted order, lowest to highest, 
and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

Note: Duplicate numbers are not counted as increasing subsequence.
'''

for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    LIS = [1]*n
    for i in range(1, len(a)):
        for j in range(0, i):
            if a[j] < a[i]:
                LIS[i] = max(LIS[i], LIS[j]+1)
    print(max(LIS))