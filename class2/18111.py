import sys
from collections import Counter

N, M, B = map(int, input().split(" "))

ground = []
for _ in range(N):
    ground.extend(map(int, sys.stdin.readline().rstrip().split()))

ground_blocks = sum(ground)
ground = Counter(ground)

best_time = 256 * 500 * 500 * 2
best_h = 256

for try_h in range(max(ground), min(ground) - 1, -1):
    blocks_gain = ground_blocks - try_h * N * M
    if blocks_gain < -B: continue

    punch_actions = sum((h - try_h) * c for h, c in ground.items() if h > try_h)
    place_actions = sum((try_h - h) * c for h, c in ground.items() if h < try_h)

    time = 2 * punch_actions + place_actions

    if time < best_time: best_time, best_h = time, try_h

print(best_time, best_h)
