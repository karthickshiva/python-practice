# To find the sub array in the given array having negative numbers with the given sum

x = [1, -10, 8, 9, -19, 8, 0, -1]
k = 7
sum = [0]

for i in range(len(x)):
    sum.append(sum[i]+x[i])

found = False

for i in range(len(x)):
    for j in range(i, len(x)):
        sub_sum = sum[j+1] - sum[i]
        print [i,j]
        if sub_sum == k:
            found = True
            print "found" 

if not found:
    print "Not found"