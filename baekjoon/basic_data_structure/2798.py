N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))

res = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      temp_res = cards[i] + cards[j] + cards[k]
      if temp_res <= M:
        res = max(res, temp_res)

print(res)