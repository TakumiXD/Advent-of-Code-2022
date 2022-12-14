from collections import defaultdict

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    ROW = len(inputs)
    COL = len(inputs[0])

    left = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    right = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    top = [ [ -1 for i in range(COL) ] for j in range(ROW) ]
    bottom = [ [ -1 for i in range(COL) ] for j in range(ROW) ]

    stack = []

    for i in range(ROW):
        stack.clear()
        for j in range(COL):
            while stack and inputs[i][stack[-1]] <= inputs[i][j]:
                poppedIndex = stack.pop()
                left[i][poppedIndex] = j
            stack.append(j)

    for i in range(ROW):
        stack.clear()
        for j in range(COL - 1, -1, -1):
            while stack and inputs[i][stack[-1]] <= inputs[i][j]:
                poppedIndex = stack.pop()
                right[i][poppedIndex] = j
            stack.append(j)

    for j in range(COL):
        stack.clear()
        for i in range(ROW):
            while stack and inputs[stack[-1]][j] <= inputs[i][j]:
                poppedIndex = stack.pop()
                top[poppedIndex][j] = i
            stack.append(i)


    for j in range(COL):
        stack.clear()
        for i in range(ROW - 1, -1, -1):
            while stack and inputs[stack[-1]][j] <= inputs[i][j]:
                poppedIndex = stack.pop()
                top[poppedIndex][j] = i
            stack.append(i)

    res = 0

    for i in range(ROW):
        for j in range(COL):
            leftScore = left[i][j] - j if left[i][j] > 0 else COL - j - 1
            rightScore = j - right[i][j] if right[i][j] > 0 else j
            topScore = top[i][j] - i if top[i][j] > 0 else ROW - i - 1
            bottomScore = i - bottom[i][j] if bottom[i][j] > 0 else i
            score = leftScore * rightScore * topScore * bottomScore
            res = max(res, score)

    print(res)