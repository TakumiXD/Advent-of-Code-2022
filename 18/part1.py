with open("input.txt", "r") as f:
    input = f.read().splitlines()

    cubes = []
    for line in input:
        x, y, z = line.replace(","," ").split(" ")
        cubes.append((int(x), int(y), int(z)))

    used = set()
    surfaceArea = 0

    offsets = [ (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1) ]

    for x, y, z in cubes:
        for dx, dy, dz in offsets:
            surfaceArea = surfaceArea + 1 if (x + dx, y + dy, z + dz) not in used else surfaceArea - 1
        used.add((x, y, z))

    print(surfaceArea)