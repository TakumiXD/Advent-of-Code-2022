with open("input.txt", "r") as f:
    input = f.read().splitlines()

    DECRYPTION_KEY = 811589153
    sequence = [ (i, int(x) * DECRYPTION_KEY) for i, x in enumerate(input) ]
    original = sequence.copy()
    SIZE_OF_INPUT = len(sequence)
    NUM_OF_MIXES = 10

    numOfMixes = 0
    for _ in range(NUM_OF_MIXES):
        for i, jumpSize in original:
            for swapIndex1, (j, x) in enumerate(sequence):
                if (j, x) == (i, jumpSize):
                    break
            swapIndex2 = (swapIndex1 + jumpSize) % (SIZE_OF_INPUT - 1)
            if swapIndex2 == 0:
                swapIndex2 = SIZE_OF_INPUT - 1
            sequence.pop(swapIndex1)
            sequence.insert(swapIndex2, (i, jumpSize))

    indicesToCheck = [1000, 2000, 3000]

    indexOfZero = 0
    for i, (j, x) in enumerate(sequence):
        if x == 0:
            indexOfZero = i

    res = 0
    for i in indicesToCheck:
        res += (sequence[(indexOfZero + i) % SIZE_OF_INPUT][1])

    print(res)