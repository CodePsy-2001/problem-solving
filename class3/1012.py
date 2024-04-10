from collections import deque

def cover_bundles_bfs(start_coord: tuple, initial_field: dict) -> dict:
    field = initial_field.copy()
    field.pop(start_coord)

    queue = deque([start_coord])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in field:
                field.pop((nx, ny))
                queue.append((nx, ny))

    return field

T = int(input())
for _ in range(T):
    _, _, K = map(int, input().split())

    field = dict()
    for _ in range(K):
        x, y = map(int, input().split())
        field[(x, y)] = 1

    bundles = 0
    while field:
        coord = next(iter(field))
        field = cover_bundles_bfs(coord, field)
        bundles += 1

    print(bundles)