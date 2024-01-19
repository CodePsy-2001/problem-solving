n = int(input())
toBes = [int(input()) for _ in range(n)]

i = 0
stack = [0]
log = []

def push():
  global i
  i += 1
  stack.append(i)
  log.append("+")

def pop():
  p = stack.pop()
  log.append("-")
  return p

for toBe in toBes:
  while stack[-1] < toBe:
    push()
  if stack[-1] > toBe:
    print("NO")
    exit()
  if stack[-1] == toBe: pop()
  
for l in log: print
