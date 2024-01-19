# 1654번: 랜선 자르기
# 이미 가지고 있는 전선 k개를 잘라, 같은 길이의 전선 n개를 만들려고 한다. 이때 전선의 최대 길이(l)는?

def check(wires: list, l: int) -> int:
    return sum(wire // l for wire in wires)

k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]

start, end = 1, max(wires)

while start <= end:
    mid = (start + end) // 2
    if (check(wires, mid) >= n): start = mid + 1
    else: end = mid - 1;

print(end)
