import re

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    PATTERN = re.compile(r"-?\d+")
    SIZE = 0
    TIME_LIMIT = 24

    oreRobot = {}
    clayRobot = {}
    obsidianRobot = {}
    geodeRobot = {}
    maxOre = {}
    dp = {}

    for line in input:
        blueprint, oR, cR, obsR1, obsR2, gR1, gr2 = map(int, PATTERN.findall(line))
        oreRobot[blueprint] = oR
        clayRobot[blueprint] = cR
        obsidianRobot[blueprint] = (obsR1, obsR2)
        geodeRobot[blueprint] = (gR1, gr2)
        maxOre[blueprint] = max(oR, cR, obsR1, gR1)
        SIZE += 1


    def dfs(blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum, oreNum, clayNum, obsNum, geoNum):
        # optimization 1
        if (blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum, oreNum, clayNum, obsNum, geoNum) in dp:
            return dp [(blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum, oreNum, clayNum, obsNum, geoNum)]
        minute += 1
        # base case
        if minute == TIME_LIMIT:
            return geoNum + geoRobNum
        # optimization 2
        if (oreRobNum > maxOre[blueprint]) or (clayRobNum > obsidianRobot[blueprint][1]) or (oreRobNum > geodeRobot[blueprint][1]):
            return geoNum + geoRobNum
        # Case 1: don't construct any robots
        res = max(geoNum + geoRobNum, 
            dfs(blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum, oreNum + oreRobNum, clayNum + clayRobNum, obsNum + obsRobNum, geoNum + geoRobNum))
        TIME_LEFT = TIME_LIMIT - minute
        skipOre = False
        skipClay = False
        skipObsidian = False
        if (oreNum + oreRobNum * TIME_LEFT) > (TIME_LEFT * maxOre[blueprint]):
            skipOre = True
        if (clayNum + clayRobNum * TIME_LEFT) > (TIME_LEFT * obsidianRobot[blueprint][1]):
            skipClay = True
        if (obsNum + obsRobNum * TIME_LEFT) > (TIME_LEFT * geodeRobot[blueprint][1]):
            skipObsidian = True
        # Case 2: construct a ore robot if possible
        if oreNum >= oreRobot[blueprint] and not skipOre:
            res = max(res, 
                dfs(blueprint, minute, oreRobNum + 1, clayRobNum, obsRobNum, geoRobNum, oreNum + oreRobNum - oreRobot[blueprint], clayNum + clayRobNum, obsNum + obsRobNum, geoNum + geoRobNum))
        # Case 3: construct a clay robot if possible
        if oreNum >= clayRobot[blueprint] and not skipClay:
            res = max(res, 
                dfs(blueprint, minute, oreRobNum, clayRobNum + 1, obsRobNum, geoRobNum, oreNum + oreRobNum - clayRobot[blueprint], clayNum + clayRobNum, obsNum + obsRobNum, geoNum + geoRobNum))
        # Case 4: construct an obsidian robot if possible
        if oreNum >= obsidianRobot[blueprint][0] and clayNum >= obsidianRobot[blueprint][1] and not skipObsidian:
            res = max(res, 
                dfs(blueprint, minute, oreRobNum, clayRobNum, obsRobNum + 1, geoRobNum, oreNum + oreRobNum - obsidianRobot[blueprint][0], clayNum + clayRobNum - obsidianRobot[blueprint][1], obsNum + obsRobNum, geoNum + geoRobNum))
        # Case 5: construct a geode robot if possible
        if oreNum >= geodeRobot[blueprint][0] and obsNum >= geodeRobot[blueprint][1]:
            res = max(res, 
                dfs(blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum + 1, oreNum + oreRobNum - geodeRobot[blueprint][0], clayNum + clayRobNum, obsNum + obsRobNum - geodeRobot[blueprint][1], geoNum + geoRobNum))
        # cache using pre incremented minute/time
        minute -= 1
        dp[(blueprint, minute, oreRobNum, clayRobNum, obsRobNum, geoRobNum, oreNum, clayNum, obsNum, geoNum)] = res
        return res

    res = 0
    for ID in range(1, SIZE + 1):
        largestNumOfGeodes = dfs(ID, 0, 1, 0, 0, 0, 0, 0, 0, 0)
        qualityLevel = ID * largestNumOfGeodes
        res += qualityLevel
        dp.clear()

    print(res)