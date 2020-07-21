answer = -1

def is_changable(word1, word2):
  diff_cnt = 0
  for i in range(len(word1)):
    if word1[i] != word2[i]:
      diff_cnt = diff_cnt + 1

  if diff_cnt == 1:
    return True
  else:
    return False

def dfs(depth, curr, target, words, visited):
  global answer
  if curr == target:
    if answer == -1:
      answer = depth
    else:
      answer = min(answer, depth)
    return

  for i in range(len(words)):
    if not visited[i] and is_changable(curr, words[i]):
      visited[i] = True
      dfs(depth+1, words[i], target, words, visited)
      visited[i] = False

def solution(begin, target, words):
  visited = [False for i in range(len(words))]
  dfs(0, begin, target, words, visited)

  if answer == -1:
    return 0
  else:
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))