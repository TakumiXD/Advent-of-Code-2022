with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    shapeScore = { "X": 1, 
                   "Y": 2, 
                   "Z": 3 }

    outcomeScore = { ("A", "X"): 3,
                     ("A", "Y"): 6,
                     ("A", "Z"): 0,
                     ("B", "X"): 0,
                     ("B", "Y"): 3,
                     ("B", "Z"): 6,
                     ("C", "X"): 6,
                     ("C", "Y"): 0,
                     ("C", "Z"): 3}

    res = 0
    for input in inputs:
        fst, snd = input.split(" ")
        res += shapeScore[snd]
        res += outcomeScore[fst, snd]

    print(res)