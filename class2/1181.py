N = int(input())
words = [input() for _ in range(N)]

words.sort()
words.sort(key=len)

result = []
for w in words:
  if w not in result:
    result.append(w)
    print(w)
