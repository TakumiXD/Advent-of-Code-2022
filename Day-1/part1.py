with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    curr = 0
    maxVal = -1

    for input in inputs:
        if input == "":
            maxVal = max(maxVal, curr)
            curr = 0
        else:
            curr += int(input)

    print(maxVal)