with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    itemsInFst = set()
    itemsInFstAndSnd = set()
    res = 0
    index = -1

    for input in inputs:
        index += 1
        match index:
            case 0:
                for char in input:
                    itemsInFst.add(char)
            case 1:
                for char in input:
                    if char in itemsInFst:
                        itemsInFstAndSnd.add(char)
            case 2: 
                for char in input:
                    if char in itemsInFstAndSnd:
                        if ord(char) < ord('a'):
                            res += (ord(char) - ord('A') + 27)
                        else:
                            res += (ord(char) - ord('a') + 1)
                        break
                itemsInFst.clear()
                itemsInFstAndSnd.clear()
                index = -1

    print(res)