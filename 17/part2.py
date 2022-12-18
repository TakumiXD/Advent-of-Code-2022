with open("input.txt", "r") as f:
    input = [*f.read()]

    NUM_OF_ROCKS = 1000000000000
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

    # return tuple of size 7, for each row, the maximum height minus that row's height
    def getPastHeightDiffs(maxY):
        res = []
        for height in maxInCol:
            res.append(maxY - height)
        return tuple(res)

    dp = {}

    i = 0
    rockNum = 0
    offset = 0

    while rockNum < NUM_OF_ROCKS:
        currRock = rocks[rockNum % 5]
        originalI = i
        # initial pos
        rockPos = [ (x + 2, y + maxY + 4) for x, y in currRock ]
        while True:
            # gas push
            tryRockPos = moveLeftOrRight(input[i], rockPos)
            originalI = i
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
        # cache the
        # 1. index currently in the file (jet index)
        # 2. current rock
        # 3. tuple of size 7, for each row, the maximum height minus that row's height
        # by cacheing this, the code will be able to detect a cycle
        key = (originalI, rockNum % 5, getPastHeightDiffs(maxY))
        rockNum += 1
        # when the cycle is detected, get the length of the cycle and compute the number of cycles
        # that would be left, and add their product to the rockNum. This will skip a significant
        # number of rocks. Then, compute the offset to add to the height at the very end
        if key in dp:
            lastRockNum, lastMaxY = dp[key]
            cycleLength = rockNum - lastRockNum
            cyclesLeft = (NUM_OF_ROCKS - rockNum) // cycleLength 
            rockNum += (cyclesLeft * cycleLength)
            offset = offset + (cyclesLeft * (maxY - lastMaxY))
            dp = {}
        dp[key] = (rockNum, maxY)

    print(maxY + offset)