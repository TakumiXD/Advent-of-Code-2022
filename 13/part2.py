import json

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    def compare(fst, snd):
        i = 0
        while i < min(len(fst), len(snd)):
            f = fst[i]
            s = snd[i]
            res = 0
            if type(f) == int and type(s) == int:
                if f < s:
                    res = 1
                elif f == s:
                    res = 0
                else:
                    res = -1
            else:
                if type(f) == int:
                    f = [f]
                if type(s) == int:
                    s = [s]
                res = compare(f,s)
            if res == 0:
                i += 1
                continue
            else:
                return res

        if len(fst) == len(snd):
            return 0
        elif len(snd) > len(fst):
            return 1
        else:
            return -1

    smallerThanDivider1 = 0
    smallerThanDivider2 = 0
    for line in input:
        if line == "":
            continue
        loadedLine = json.loads(line)
        if compare(loadedLine, [[2]]) == 1:
            smallerThanDivider1 += 1
            smallerThanDivider2 += 1
        elif compare(loadedLine, [[6]]) == 1:
            smallerThanDivider2 += 1

    print((smallerThanDivider1 + 1) * (smallerThanDivider2 + 2))