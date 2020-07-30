def solution(s):
  answer = 0
  n = len(s)
  for max_len in range(1, n+1):
    for start_idx in range(0, n):
      if start_idx + max_len <= n:
        curr_s = s[start_idx:(start_idx+max_len)]
        if curr_s == curr_s[::-1]:
          answer = max_len
          break

  return answer

print(solution('abacde'))