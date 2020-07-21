def solution(N, number):
  if N == number:
    return 1

  answer = -1
  dp = [set() for i in range(8+1)]
  dp[0] = {0}
  for i in range(1, len(dp)):
    dp[i].add(int(str(N)*i))

  for i in range(2, len(dp)):
    for j in range(1, i):
      for op1 in dp[j]:
        for op2 in dp[i-j]:
          dp[i].add(op1+op2)
          dp[i].add(op1-op2)
          dp[i].add(op1*op2)
          if op2 != 0:
            dp[i].add(op1//op2)
    if number in dp[i]:
      answer = i
      break

  return answer

print(solution(5, 12))