import re

with open("input.txt", "r") as f:
    # parsing
    input = f.read().splitlines()
    pattern = re.compile(r"-?\d+")
    lines = []
    for line in input:
        sensorX, sensorY, beaconX, beaconY = map(int, pattern.findall(line))
        lines.append((sensorX, sensorY, beaconX, beaconY))

    Y = 2000000
    intervals = []
    beaconsInY = set()
    numOfBeaconsInY = 0

    # get list of intervals of x coordinates at the 'Y' level that cannot have beacons  
    for line in lines:
        sensorX, sensorY, beaconX, beaconY = line
        if beaconY == Y:
            beaconsInY.add(beaconX)

        dist = abs(sensorY - beaconY) + abs(sensorX - beaconX)
        offset = dist - abs(sensorY - Y)

        if offset < 0:
            continue

        lowX = sensorX - offset
        uppX = sensorX + offset
        intervals.append([lowX, uppX])

    # sort list of intervals
    intervals.sort()
    sortedIntervals = []
    for low, upp in intervals:
        if sortedIntervals and low <= sortedIntervals[-1][1]:
            sortedIntervals[-1][1] = max(sortedIntervals[-1][1], upp)
        else:
            sortedIntervals.append([low, upp])

    # get number of beacons in the 'Y' level
    for beacon in beaconsInY:
        for low, upp in intervals:
            if low <= beacon <= upp:
                numOfBeaconsInY += 1
                break

    # get the sum of intervals and subtract the number of beacons in 'Y' level
    sumOfIntervals = 0
    for low, upp in sortedIntervals:
        diff = upp - low + 1
        sumOfIntervals += diff

    print(sumOfIntervals - numOfBeaconsInY)

