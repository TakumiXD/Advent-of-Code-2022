from collections import deque

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    ROW = len(input)
    COL = len(input[0])
    LARGE_NUM = 9999

    heightMap = [ [ 'a' for j in range(COL) ] for i in range(ROW) ]

    start = [0,0]
    end = [0,0]

    for i in range(ROW):
        for j in range(COL):
            if input[i][j] == 'S':
                heightMap[i][j] = 'a'
            elif input[i][j] == 'E':
                start[0] = i
                start[1] = j
                heightMap[i][j] = 'z'
            else:
                heightMap[i][j] = input[i][j]

    dist = [ [ LARGE_NUM for j in range(COL) ] for i in range(ROW) ]
    dist[start[0]][start[1]] = 0

    q = deque()
    q.append(start)

    while q:
        r, c = q.popleft()
        if heightMap[r][c] == 'a':
            end[0] = r
            end[1] = c
            break
        currDist = dist[r][c]
        currOrd = ord(heightMap[r][c])
        if (r > 0) and (dist[r-1][c] == LARGE_NUM) and (currOrd - ord(heightMap[r-1][c]) <= 1):
                dist[r-1][c] = currDist + 1
                q.append([r-1,c])
        if (r < ROW - 1) and (dist[r+1][c] == LARGE_NUM) and (currOrd - ord(heightMap[r+1][c]) <= 1):
                dist[r+1][c] = currDist + 1
                q.append([r+1,c])
        if (c > 0) and (dist[r][c-1] == LARGE_NUM) and (currOrd - ord(heightMap[r][c-1]) <= 1):
                dist[r][c-1] = currDist + 1
                q.append([r,c-1])    
        if (c < COL - 1) and (dist[r][c+1] == LARGE_NUM) and (currOrd - ord(heightMap[r][c+1]) <= 1):
                dist[r][c+1] = currDist + 1
                q.append([r,c+1])

    print(dist[end[0]][end[1]])