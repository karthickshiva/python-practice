for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total_sum, sum_left = sum(a), 0
    found = False
    for j in range(len(a)):
        x = a[j]
        y = total_sum - x
        if (y&1 == 0) and (y/2 == sum_left):
            print(j+1)
            found = True
            break
        sum_left += x
    if not found:
        print(-1)