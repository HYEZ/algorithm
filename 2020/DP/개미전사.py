n = 4
k = [1, 3, 1, 5]

n = 10
k = [1, 3, 1, 5, 1, 1, 4, 8, 9, 1]
d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    # 최대값 저장하기
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
    