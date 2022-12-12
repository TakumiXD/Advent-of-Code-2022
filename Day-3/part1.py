with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    itemsInFst = set()
    res = 0
    
    for input in inputs:
        fst, snd = input[:len(input)//2], input[len(input)//2:]
        for char in fst:
            itemsInFst.add(char)

        for char in snd:
            if char in itemsInFst:
                if ord(char) < ord('a'):
                    res += (ord(char) - ord('A') + 27)
                else:
                    res += (ord(char) - ord('a') + 1)
                break
        
        itemsInFst.clear()
        continue

    print(res)