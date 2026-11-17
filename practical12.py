# bubble sort
num = [12, 2, 26, 76, 98]
n = len(num)
for e in range(n - 1):
    for j in range(n - 1 - e):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print(num)

#counting sort
num = [12, 2, 26, 76, 98]
max_val = max(num)
count = [0] * (max_val + 1)
for i in num:
    count[i] += 1

sorted_num = []
for i in range(len(count)):
    sorted_num.extend([i] * count[i])
print(sorted_num)
