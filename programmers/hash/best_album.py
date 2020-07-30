from collections import defaultdict

def solution(genres, plays):
  genre_with_sum = defaultdict(int)
  genre_with_plays = defaultdict(lambda:[])

  answer = []
  i = 0
  for genre, play in zip(genres, plays):
    genre_with_sum[genre] += play
    genre_with_plays[genre].append((i, play))
    i += 1

  for genre, _ in sorted(genre_with_sum.items(), key=(lambda x: x[1]), reverse=True):
    plays = sorted(genre_with_plays[genre], key=lambda x: (x[1], -x[0]), reverse=True)
    print(plays)
    answer.append(plays[0][0])
    if len(plays) > 1:
      answer.append(plays[1][0])

  return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]))