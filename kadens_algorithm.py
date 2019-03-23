x = [8, 16, -20, -5, 8, -2, 16, 3]
sum_so_far, max_sum = 0, 0

for i in x:
    if sum_so_far + i < 0:
        sum_so_far = 0
    else:
        sum_so_far += i
        max_sum = max(max_sum, sum_so_far)

if max_sum == 0:
    print max(x)
else:
    print max_sum