with open("input.txt", "r") as f:
    input = [*f.read()]

    NUM_OF_ROCKS = 2022
    NUM_OF_GAS = len(input)
    maxY = 0
    maxInCol = [ 0 for i in range(7) ]
    used = {(0,0), (1.0), (2,0), (3,0), (4,0), (5,0), (6,0)}

    rocks = [
        [(0,0),(1,0),(2,0),(3,0)],
        [(1,0),(0,1),(1,1),(2,1),(1,2)],
        [(0,0),(1,0),(2,0),(2,1),(2,2)],
        [(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(0,1),(1,1)]
    ]

    def moveLeftOrRight(char, pos):
        if char == "<":
            return [ (x - 1, y) for x, y in pos ]
        else:
            return [ (x + 1, y) for x, y in pos ]

    def moveDown(pos):
        return [ (x, y - 1) for x, y in pos ]

    def valid(pos):
        for x, y in pos:
            if x < 0 or x > 6 or (x,y) in used:
                return False
        return True

    i = 0
    for rockNum in range(NUM_OF_ROCKS):
        currRock = rocks[rockNum % 5]
        # initial pos
        rockPos = [ (x + 2, y + maxY + 4) for x, y in currRock ]
        while True:
            # gas push
            tryRockPos = moveLeftOrRight(input[i], rockPos)
            i = (i + 1) % NUM_OF_GAS
            if valid(tryRockPos):
                rockPos = tryRockPos
            # down 1
            tryRockPos = moveDown(rockPos)
            if not valid(tryRockPos):
                break
            else:
                rockPos = tryRockPos
        for x, y in rockPos:
            used.add((x, y))
            maxInCol[x] = max(maxInCol[x], y)
        maxY = max(maxInCol)

    print(maxY)