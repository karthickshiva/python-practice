# Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

from collections import deque
for __ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = deque()
    for i in range(n):
        while d and d[0]<=i-k:
            d.popleft()
        while d and a[d[-1]]<a[i]:
            d.pop()
        d.append(i)
        if i>=k-1:
            print(a[d[0]], end=" ")
    print()
