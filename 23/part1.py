from collections import deque, defaultdict

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    board = set()
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == "#":
                board.add((i, j))

    NUM_OF_ROUNDS = 10

    def hasAdjacent(position):
        y,x = position
        N = (y - 1, x)
        NE = (y - 1, x + 1)
        NW = (y - 1, x - 1)
        S = (y + 1, x)
        SE = (y + 1, x + 1)
        SW = (y + 1, x - 1)
        W = (y, x - 1)
        E = (y, x + 1)
        return not ({N, NE, NW, S, SE, SW, W, E}.isdisjoint(board))

    def hasAdjacentNorth(position):
        y,x = position
        N = (y - 1, x)
        NE = (y - 1, x + 1)
        NW = (y - 1, x - 1)
        return (N in board) or (NE in board) or (NW in board)

    def hasAdjacentSouth(position):
        y,x = position
        S = (y + 1, x)
        SE = (y + 1, x + 1)
        SW = (y + 1, x - 1)
        return (S in board) or (SE in board) or (SW in board)

    def hasAdjacentWest(position):
        y,x = position
        NW = (y - 1, x - 1)
        SW = (y + 1, x - 1)
        W = (y, x - 1)
        return (NW in board) or (SW in board) or (W in board)

    def hasAdjacentEast(position):
        y,x = position
        NE = (y - 1, x + 1)
        SE = (y + 1, x + 1)
        E = (y, x + 1)
        return (NE in board) or (SE in board) or (E in board)

    checkDirections = deque(["N", "S", "W", "E"])

    for _ in range(NUM_OF_ROUNDS):
        proposedBoard = defaultdict(set)
        for elfPos in board:
            # first half
            if not (hasAdjacent(elfPos)):
                proposedBoard[elfPos] = {elfPos}
                continue
            # second half
            y,x = elfPos
            for j in range(4):
                newPos = 0
                foundNewPos = False
                direction = checkDirections[j]
                if direction == "N" and not hasAdjacentNorth(elfPos):
                    newPos = (y - 1, x)
                    foundNewPos = True
                elif direction == "S" and not hasAdjacentSouth(elfPos):
                    newPos = (y + 1, x)
                    foundNewPos = True
                elif direction == "W" and not hasAdjacentWest(elfPos):
                    newPos = (y, x - 1)
                    foundNewPos = True
                elif direction == "E" and not hasAdjacentEast(elfPos):
                    newPos = (y, x + 1)
                    foundNewPos = True
                if foundNewPos:
                    proposedBoard[newPos].add(elfPos)
                    break
            else:
                proposedBoard[elfPos].add(elfPos)
        checkDirections.append(checkDirections.popleft())
        board.clear()
        for key, value in proposedBoard.items():
            if len(value) == 1:
                board.add(key)
            else:
                for elem in value:
                    board.add(elem)

    minX = min(x for _,x in board)
    maxX = max(x for _,x in board)
    minY = min(y for y,_ in board)
    maxY = max(y for y,_ in board)

    height = maxY - minY + 1
    width = maxX - minX + 1
    rectangleSize = height * width
    res = rectangleSize - len(board)

    print(res)