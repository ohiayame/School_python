# 각 위치의 층(layer)을 구해 이전까지의 칸 수와 층 내 위치로 값을 계산하세요.
n = int(input())

width = len(str(n * n))

for r in range(n):
    for c in range(n):
        layer = min(r, c, n - 1 - r, n - 1 - c)
        """
            layer = min(
            r,           # 위쪽까지 거리 = 1
            c,           # 왼쪽까지 거리 = 3
            n - 1 - r,   # 아래쪽까지 거리 = 5 - 1 - 1 = 3
            n - 1 - c    # 오른쪽까지 거리 = 5 - 1 - 3 = 1
        ) 그래서 (1, 3)은 layer = 1 
        """
        
        
        # 양쪽에서 1칸씩 줄어듬
        size = n - 2 * layer
        """
        | layer |    size     |
        | ----- | ----------- |
        | 0     | 5 - 2*0 = 5 |
        | 1     | 5 - 2*1 = 3 |
        | 2     | 5 - 2*2 = 1 |

        """

        # start 계산
        # size * size: 현재 layer부터 안쪽까지 남은 칸의 개수 
        # 5: layer 1 -> 25 - 9 = 16
        start = n * n - size * size + 1
        
        # 전체 좌표 (r, c)를 layer 기준의 좌표 (local_r, local_c)로 변환
        local_r = r - layer
        local_c = c - layer

        if size == 1:
            value = start

        elif local_r == 0:
            # 위쪽 줄: 왼쪽 → 오른쪽
            value = start + local_c

        elif local_c == size - 1:
            # 오른쪽 줄: 위 → 아래
            value = start + (size - 1) + local_r

        elif local_r == size - 1:
            # 아래쪽 줄: 오른쪽 → 왼쪽
            value = start + 2 * (size - 1) + (size - 1 - local_c)

        else:
            # 왼쪽 줄: 아래 → 위
            value = start + 3 * (size - 1) + (size - 1 - local_r)

        print(f"{value:>{width}}", end="")

        if c != n - 1:
            print(" ", end="")

    print()