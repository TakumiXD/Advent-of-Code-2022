with open("input.txt", "r") as f:
    input = f.read()

    for i in range(len(input)):
        subinput = input[i:i+4]
        cardinality = set(subinput)
        if len(cardinality) == 4:
            print(i+4)
            break