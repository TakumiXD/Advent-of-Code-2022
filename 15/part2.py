import re

with open("input.txt", "r") as f:
    # parsing
    input = f.read().splitlines()
    pattern = re.compile(r"-?\d+")
    lines = []
    for line in input:
        sensorX, sensorY, beaconX, beaconY = map(int, pattern.findall(line))
        lines.append((sensorX, sensorY, beaconX, beaconY))

    intervals = []
    sortedIntervals = []
    SEARCH_LOW_BOUND = 0
    SEARCH_UPP_BOUND = 4000001

    def getSignal():
        for Y in range(SEARCH_UPP_BOUND + 1):
            intervals.clear()
            sortedIntervals.clear()
            # get list of intervals of x coordinates at the 'Y' level that cannot have beacons  
            for line in lines:
                sensorX, sensorY, beaconX, beaconY = line
                dist = abs(sensorY - beaconY) + abs(sensorX - beaconX)
                offset = dist - abs(sensorY - Y)

                if offset < 0:
                    continue

                lowX = max(sensorX - offset, SEARCH_LOW_BOUND)
                uppX = min(sensorX + offset, SEARCH_UPP_BOUND)

                if uppX < 0:
                    continue
                
                intervals.append([lowX, uppX])

            # sort list of intervals
            intervals.sort()
            for low, upp in intervals:
                if sortedIntervals and low <= sortedIntervals[-1][1]:
                    sortedIntervals[-1][1] = max(sortedIntervals[-1][1], upp)
                else:
                    sortedIntervals.append([low, upp])

            # if there is a gap in the intervals
            if len(sortedIntervals) != 1:
                return(sortedIntervals[0][1]+1, Y)
        return (0,0)

    x,y = getSignal()
    print(x*SEARCH_UPP_BOUND+y)

