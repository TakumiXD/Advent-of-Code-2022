from collections import deque
from math import lcm

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    blizzardLeft = set()
    blizzardTop = set()
    blizzardRight = set()
    blizzardDown = set()
    for i, line in enumerate(input[1:]):
        for j, char in enumerate(line[1:]):
            if char == "<":
                blizzardLeft.add((i, j))
            elif char == "^":
                blizzardTop.add((i, j))
            elif char == ">":
                blizzardRight.add((i, j))
            elif char == "v":
                blizzardDown.add((i, j))

    ROW = len(input) - 2
    COL = len(input[0]) - 2
    start = (-1, 0)
    end = (ROW, COL - 1)
    lcm = lcm(ROW, COL)

    dp = set()

    q = deque()
    q.append((0, start[0], start[1]))
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]

    def collideLeft(minute, row, col):
        tr, tc = 0, -1
        return (row, (col + minute) % COL) in blizzardLeft

    def collideTop(minute, row, col):
        tr, tc = -1, 0
        return ((row + minute) % ROW, col) in blizzardTop

    def collideRight(minute, row, col):
        tr, tc = 0, 1
        return (row, (col - minute) % COL) in blizzardRight

    def collideDown(minute, row, col):
        tr, tc = 1, 0
        return ((row - minute) % ROW, col) in blizzardDown

    def main(start, goal, minute):
        res = 0
        while q:
            minute, row, col = q.popleft()
            minute += 1

            for addRow, addCol in offsets:
                newRow = row + addRow
                newCol = col + addCol
                if (newRow, newCol) == goal:
                    res = minute
                    break

                if ((newRow, newCol) != start) and (newRow < 0 or newRow >= ROW or newCol < 0 or newCol >= COL):
                    continue

                if not ((collideTop(minute, newRow, newCol) or collideDown(minute, newRow, newCol) 
                    or collideLeft(minute, newRow, newCol) or collideRight(minute, newRow, newCol))):
                    key = (minute, newRow, newCol)
                    if key in dp:
                        continue
                    q.append(key)
                    dp.add(key)
            if res != 0:
                break
        return res

    nextMin = main(start, end, 0)
    dp.clear()
    q.clear()
    q.append((nextMin, end[0], end[1]))
    nextMin = main(end, start, nextMin)
    dp.clear()
    q.clear()
    q.append((nextMin, start[0], start[1]))
    print(main(start, end, nextMin))