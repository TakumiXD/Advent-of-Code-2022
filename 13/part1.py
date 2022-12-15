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

    i = 0
    res = 0
    while i < len(input):
        fst = json.loads(input[i])
        snd = json.loads(input[i+1])
        if compare(fst, snd) == 1:
            res += (i // 3 + 1)
        i += 3

    print(res)