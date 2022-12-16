with open("input.txt", "r") as f:
    input = f.read().splitlines()

    cave = set()
    pouringFrom = (500,0)
    abyssY = 0

    # building the cave and setting y coordinate of abyss
    for line in input:
        editedLine = [x.split(",") for x in line.split(" -> ")]
        pairs = [(int(x[0]), int(x[1])) for x in editedLine]
        for pair1, pair2 in zip(pairs, pairs[1:]):
            fst1, snd1 = pair1
            fst2, snd2 = pair2
            abyssY = max(snd1, snd2, abyssY)
    
            for x in range(min(fst1, fst2), max(fst1, fst2) + 1):
                cave.add((x, snd1))
    
            for y in range(min(snd1, snd2), max(snd1, snd2) + 1):
                cave.add((fst1, y))
    abyssY = abyssY + 2

    # building floor
    for i in range(-1000, 1000):
        cave.add((i,abyssY))

    def drop(coord):
        if coord in cave:
            return False
        coordinate = coord
        # go down as much as possible
        while coordinate not in cave:
            coordinate = (coordinate[0], coordinate[1] + 1)
        coordinate = (coordinate[0], coordinate[1] - 1)
        # try left
        if drop((coordinate[0] - 1, coordinate[1] + 1)):
            return True
        # try right
        elif drop((coordinate[0] + 1, coordinate[1] + 1)):
            return True
        else:
            cave.add(coordinate)
            return True

    res = 0

    while drop(pouringFrom):
        res += 1

    print(res)