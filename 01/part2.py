with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    curr = 0
    allVals = []

    for input in inputs:
        if input == "":
            allVals.append(curr)
            curr = 0
        else:
            curr += int(input)

    allVals.sort(reverse=True)
    print(sum(allVals[:3]))