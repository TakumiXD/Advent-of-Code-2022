from collections import deque

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    TIME_LIMIT = 26
    flowRates = {}
    posFlowRates = set()
    tunnels = {}
    dp = {}

    for line in input:
        line = line.split(" ")
        valve = line[1]
        flowRate = int(line[4].replace("rate=","").replace(";",""))
        if flowRate > 0:
            posFlowRates.add(valve)
        tunnel = [ s.replace(",", "") for s in line[9:] ]
        flowRates[valve] = flowRate
        tunnels[valve] = tunnel

    # distance from a valve to all valves with a positive flow rate
    dist = {}

    # BFS to set the dist hash map
    for valve, flowRate in flowRates.items():
        if valve != "AA" and flowRate == 0:
            continue

        dist[valve] = {}
        dist[valve][valve] = 0
        dist[valve]["AA"] = 0

        visited = set()
        visited.add(valve)

        q = deque()
        q.append((0, valve))

        while q:
            distance, v = q.popleft()
            for neighbor in tunnels[v]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if flowRates[neighbor] > 0:
                    dist[valve][neighbor] = distance + 1
                q.append((distance + 1, neighbor))

        dist[valve].pop(valve, None)
        dist[valve].pop("AA", None)
        
    # used for bit masking
    bitIndex = {}
    for index, element in enumerate(posFlowRates):
        bitIndex[element] = index

    # because the opened valves can't be memoized, use bit masking to keep track of opened valves
    def dfs(valve, openedBitMask, minute):
        if (valve, openedBitMask, minute) in dp:
            return dp[(valve, openedBitMask, minute)]

        # base case
        if minute == TIME_LIMIT:
            return 0

        res = 0
        for neighbor in dist[valve]:
            bit = 1 << bitIndex[neighbor]
            # if valve is opened
            if openedBitMask & bit:
                continue
            remainingTime = TIME_LIMIT - minute - dist[valve][neighbor] - 1
            if remainingTime <= 0:
                continue
            # recurse
            res = max(res, dfs(neighbor, openedBitMask | bit, minute + dist[valve][neighbor] + 1) + (flowRates[neighbor] * remainingTime))

        dp[(valve, openedBitMask, minute)] = res
        return res
        
    res = 0

    # try every two subset partition of the available valves and compute the max
    b = (1 << len(posFlowRates)) - 1
    for i in range((b + 1) // 2):
        res = max(res, dfs("AA", i, 0) + dfs("AA", b ^ i, 0))

    print(res)