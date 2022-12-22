from operator import add, sub, mul, truediv

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    yell = {}
    function = lambda a, b, op: {"+": add, "-": sub, "*": mul, "/": truediv} [op](a, b)

    # computes what number the monkey will yell
    def getYell(monkey):
        res = yell[monkey]
        if type(res) == list:
            return function(getYell(res[0]), getYell(res[1]), res[2])
        else:
            return res

    # parsing and setting "yell" hash map
    for line in input:
        line = line.split(" ")
        monkey = line[0].replace(":", "")
        if line[1].isdigit():
            yell[monkey] = int(line[1])
        else:
            op = line[2]
            a = line[1]
            b = line[3]
            yell[monkey] = [a, b, op]

    print(getYell("root"))