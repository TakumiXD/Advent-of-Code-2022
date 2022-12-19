from collections import deque

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    cubes = []
    minX = minY = minZ = maxX = maxY = maxZ = -1
    for line in input:
        x, y, z = line.replace(","," ").split(" ")
        maxX = max(maxX, int(x) + 1)
        maxY = max(maxY, int(y) + 1)
        maxZ = max(maxZ, int(z) + 1)
        cubes.append((int(x), int(y), int(z)))

    usedCubes = set()
    usedSurfaces = set()
    surfaceArea = 0

    offsets = [ (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1) ]

    for x, y, z in cubes:
        for dx, dy, dz in offsets:
            surfaceArea = surfaceArea + 1 if (x + dx, y + dy, z + dz) not in usedCubes else surfaceArea - 1
            usedSurfaces.add((x + dx / 2, y + dy / 2, z + dz / 2))
        usedCubes.add((x, y, z))

    reachableCubes = set()
    reachableCubes.add((minX, minY, minZ))
    q = deque()
    q.append((minX, minY, minZ))

    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in offsets:
            offsetX = x + dx 
            offsetY = y + dy
            offsetZ = z + dz
            if ((not (minX <= offsetX <= maxX and minY <= offsetY <= maxY and minZ <= offsetZ <= maxZ)) or 
                ((offsetX, offsetY, offsetZ) in reachableCubes) or ((offsetX, offsetY, offsetZ) in usedCubes)):
                continue
            reachableCubes.add((offsetX, offsetY, offsetZ))
            q.append((offsetX, offsetY, offsetZ))

    reachableSurfaces = set()

    for x, y, z in reachableCubes:
        for dx, dy, dz in offsets:
            reachableSurfaces.add((x + dx / 2, y + dy / 2, z + dz / 2))

    outsideSurfaces = reachableSurfaces.intersection(usedSurfaces)
    print(len(outsideSurfaces))