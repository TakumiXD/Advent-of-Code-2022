with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    stack = [ [] for i in range(9) ] 
    for i in range(7, -1, -1):
        for j in range(9):
            if lines[i][j*4 + 1] != " ":
                stack[j].append(lines[i][j*4 + 1])

    for i in range(10, len(lines)):
        line = lines[i]
        moveVal, fromVal, toVal = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        for j in range(int(moveVal)):
            poppedVal = stack[int(fromVal) - 1].pop()
            stack[int(toVal) - 1].append(poppedVal)

    res = ''
    for i in range(9):
        res += stack[i][-1]

    print(res)