with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    outcomeScore = { "X": 0, 
                     "Y": 3, 
                     "Z": 6 }

    shapeScore = { ("A", "X"): 3,
                   ("A", "Y"): 1,
                   ("A", "Z"): 2,
                   ("B", "X"): 1,
                   ("B", "Y"): 2,
                   ("B", "Z"): 3,
                   ("C", "X"): 2,
                   ("C", "Y"): 3,
                   ("C", "Z"): 1}

    res = 0
    for input in inputs:
        fst, snd = input.split(" ")
        res += outcomeScore[snd]
        res += shapeScore[fst, snd]

    print(res)