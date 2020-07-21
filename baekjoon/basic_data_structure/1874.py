n = int(input())

cnt = 1
st = []
res = []

for i in range(n):
  data = int(input())
  while cnt <= data:
    st.append(cnt)
    cnt = cnt+1
    res.append('+')
  if st[-1] == data:
    st.pop()
    res.append('-')
  else:
    print('NO')
    exit()

for r in res:
  print(r)