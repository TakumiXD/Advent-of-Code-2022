with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    ROW = len(inputs)
    COL = len(inputs[0])

    left = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    right = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    top = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    bottom = [ [ -1 for i in range(COL) ] for j in range(ROW) ]

    for i in range(ROW):
        maxInRow = -1
        for j in range(COL):
            left[i][j] = maxInRow
            maxInRow = max(maxInRow, int(inputs[i][j]))

    for i in range(ROW):
        maxInRow = -1
        for j in range(COL - 1, -1, -1):
            right[i][j] = maxInRow
            maxInRow = max(maxInRow, int(inputs[i][j]))

    for j in range(COL):
        maxInCol = -1
        for i in range(ROW):
            top[i][j] = maxInCol
            maxInCol = max(maxInCol, int(inputs[i][j]))

    for j in range(COL):
        maxInCol = -1
        for i in range(ROW - 1, -1, -1):
            bottom[i][j] = maxInCol
            maxInCol = max(maxInCol, int(inputs[i][j]))

    res = 0
    for i in range(ROW):
        for j in range(COL):
            if (int(inputs[i][j]) > left[i][j] or  int(inputs[i][j]) > right[i][j]
                or int(inputs[i][j]) > top[i][j] or int(inputs[i][j]) > bottom[i][j]):
                res += 1

    print(res)