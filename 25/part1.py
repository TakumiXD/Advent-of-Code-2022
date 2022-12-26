with open("input.txt", "r") as f:
    input = f.read().splitlines()

    sum = 0

    for line in input:
        sumOfLine = 0
        index = 0
        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            power = 5 ** index
            coefficient = 0
            if char == "=":
                coefficient = -2
            elif char == "-":
                coefficient = -1
            else:
                coefficient = int(char)
            sumOfLine += coefficient * power
            index += 1
        sum += sumOfLine

    res = ""
    while sum:
        remainder = sum % 5
        sum //= 5

        if remainder <= 2:
            res = str(remainder) + res
        elif remainder == 3:
            res = "=" + res
            sum += 1
        elif remainder == 4:
            res = "-" + res
            sum += 1

    print(res)       