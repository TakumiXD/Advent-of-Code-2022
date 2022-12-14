with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    cycle = 0
    X = 1
    res = 0
    cycleToCheck = 20

    for line in lines:
        cycle += 1
        if cycle == cycleToCheck:
            res += (cycleToCheck * X)
            cycleToCheck += 40
        if line[:4] == "addx":
            cycle += 1
            if cycle == cycleToCheck:
                res += (cycleToCheck * X)
                cycleToCheck += 40
            addVal = int(line.split(" ")[1])
            X += addVal

    print(res)