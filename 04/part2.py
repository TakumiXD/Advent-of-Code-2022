with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    res = 0
    for line in lines:
        fst, snd = line.split(',')
        fstLow, fstUpp = fst.split('-')
        sndLow, sndUpp = snd.split('-')
        fstLow, fstUpp, sndLow, sndUpp = int(fstLow), int(fstUpp), int(sndLow), int(sndUpp)
        if (fstUpp >= sndLow and fstLow <= sndUpp):
            res += 1

    print(res)