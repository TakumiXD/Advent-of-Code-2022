import re
from collections import defaultdict

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    COL = 0
    ROW = 0
    leftEdge = defaultdict(lambda: 9999)
    rightEdge = defaultdict(lambda: 0)
    topEdge = defaultdict(lambda: 9999)
    bottomEdge = defaultdict(lambda: 0)
    for row, line in enumerate(input):
        if line != "":
            COL = max(COL, len(line))
            ROW += 1
            for col, elem in enumerate(line):
                if elem != " ":
                    leftEdge[row] = min(leftEdge[row], col)
                    rightEdge[row] = max(rightEdge[row], col)
                    topEdge[col] = min(topEdge[col], row)
                    bottomEdge[col] = max(bottomEdge[col], row)        
        else:
            break

    description = []
    pattern = re.compile(r"(\d+)([RL]?)")
    for i in range(ROW + 1, len(input)):
        line = input[i]
        description.extend(pattern.findall(line))

    col = 0
    row = 0
    while input[0][col] == " ":
        col += 1

    facingDirection = 0
    originalRow = 0
    originalCol = 0
    for num, letter in description:
        for i in range(int(num)):
            originalRow = row
            originalCol = col
            if facingDirection == 0:
                col += 1
                if col > rightEdge[row]:
                    col = leftEdge[row]
            elif facingDirection == 1:
                row += 1
                if row > bottomEdge[col]:
                    row = topEdge[col]
            elif facingDirection == 2:
                col -= 1
                if col < leftEdge[row]:
                    col = rightEdge[row]
            else:
                row -= 1
                if row < topEdge[col]:
                    row = bottomEdge[col]

            if input[row][col] == "#":
                row = originalRow
                col = originalCol
                break
        
        if letter == "R":
            facingDirection = (1, 2, 3, 0)[facingDirection]
        elif letter == "L":
            facingDirection = (3, 0, 1, 2)[facingDirection]

    res = (1000 * (row + 1)) + (4 * (col + 1)) + facingDirection

    print(res)