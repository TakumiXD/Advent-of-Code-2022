with open("input.txt", "r") as f:
    input = f.read()

    for i in range(len(input)):
        subinput = input[i:i+14]
        cardinality = set(subinput)
        if len(cardinality) == 14:
            print(i+14)
            break