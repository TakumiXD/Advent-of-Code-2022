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
            originalDirection = facingDirection
            if facingDirection == 0:
                col += 1
                if col > rightEdge[row]:
                    if 0 <= row <= 49:
                        facingDirection = 2
                        row = 149 - row
                        col = 99
                    elif 50 <= row <= 99:
                        facingDirection = 3
                        col = row + 50
                        row = 49
                    elif 100 <= row <= 149:
                        facingDirection = 2
                        row = 149 - row
                        col = 149
                    elif 150 <= row <= 199:
                        facingDirection = 3
                        col = row - 100
                        row = 149
            elif facingDirection == 1:
                row += 1
                if row > bottomEdge[col]:
                    if 0 <= col <= 49:
                        row = 0
                        col = col + 100
                    elif 50 <= col <= 99:
                        facingDirection = 2
                        row = col + 100
                        col = 49
                    elif 100 <= col <= 149:
                        facingDirection = 2
                        row = col - 50
                        col = 99
            elif facingDirection == 2:
                col -= 1
                if col < leftEdge[row]:
                    if 0 <= row <= 49:
                        facingDirection = 0
                        col = 0
                        row = 149 - row
                    elif 50 <= row <= 99:
                        facingDirection = 1
                        col = row - 50
                        row = 100
                    elif 100 <= row <= 149:
                        facingDirection = 0
                        col = 50
                        row = 149 - row
                    elif 150 <= row <= 199:
                        facingDirection = 1
                        col = row - 100
                        row = 0
            elif facingDirection == 3:
                row -= 1
                if row < topEdge[col]:
                    if 0 <= col <= 49:
                        facingDirection = 0
                        row = col + 50
                        col = 50
                    elif 50 <= col <= 99:
                        facingDirection = 0
                        row = col + 100
                        col = 0
                    elif 100 <= col <= 149:
                        row = 199
                        col = col - 100
                    
            if input[row][col] == "#":
                row = originalRow
                col = originalCol
                facingDirection = originalDirection
                break
        
        if letter == "R":
            facingDirection = (1, 2, 3, 0)[facingDirection]
        elif letter == "L":
            facingDirection = (3, 0, 1, 2)[facingDirection]

    res = (1000 * (row + 1)) + (4 * (col + 1)) + facingDirection

    print(res)