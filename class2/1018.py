# 1018번: 체스판 다시 칠하기
from itertools import product

n, m = map(int, input().split())
board = [input() for _ in range(n)]

results = []
for i, j in product(range(n - 7), range(m - 7)):
    board_8x8 = [line[j:j + 8] for line in board[i:i + 8]]

    diff = sum(board_8x8[k][l] != 'WB'[(k + l) % 2] for k, l in product(range(8), range(8)))
    diff = min(diff, 64 - diff)

    results.append(diff)

print(min(results))
