from operator import add, sub, mul, truediv, eq

with open("input.txt", "r") as f:
    input = f.read().splitlines()

    yell = {}
    # key: monkey, value: boolean indicating whether or not any of its sub monkeys yell "humn"
    yellsHumnMap = {}
    function = lambda a, b, op: {"+": add, "-": sub, "*": mul, "/": truediv, "=": eq} [op](a, b)

    # setting "yellsHumnMap" hash map
    def yellsHumn(monkey):
        res = yell[monkey]
        if type(yell[monkey]) == list:
            # not grouping them in one line because I want to exhaust the monkeys and not let "or" make the
            # function return early
            recurse1 = res[0] == "humn"
            recurse2 = res[1] == "humn"
            recurse3 = yellsHumn(res[0])
            recurse4 = yellsHumn(res[1])
            yellsHumnMap[monkey] = recurse1 or recurse2 or recurse3 or recurse4
            return yellsHumnMap[monkey]
        else:
            yellsHumnMap[monkey] = monkey == "humn"
            return yellsHumnMap[monkey]

    # computes what number the monkey will yell
    def getYell(monkey):
        res = yell[monkey]
        if type(yell[monkey]) == list:
            return function(getYell(res[0]), getYell(res[1]), res[2])
        else:
            return res

    # helper function to compute inverses of operations
    def inverseOperationOf(a, b, c, operation):
        if operation == "+":
            if a:
                return c - a
            else:
                return c - b
        if operation == "-":
            if a:
                return a - c
            else:
                return b + c
        if operation == "*":
            if a:
                return c / a
            else:
                return c / b
        if operation == "/":
            if a:
                return a / c
            else:
                return c * b

    # main recursive function to compute "humn"
    def compute(monkey, y):
        res = yell[monkey]
        if res[0] == "humn":
            return inverseOperationOf(None, getYell(res[1]), y, res[2])
        elif res[1] == "humn":
            return inverseOperationOf(getYell(res[0]), None, y, res[2])
        elif yellsHumnMap[res[0]]:
            y = inverseOperationOf(None, getYell(res[1]), y, res[2])
            return compute(res[0], y)
        else:
            y = inverseOperationOf(getYell(res[0]), None, y, res[2])
            return compute(res[1], y)

    # parsing and setting "yell" hash map
    for line in input:
        line = line.split(" ")
        monkey = line[0].replace(":", "")
        if line[1].isdigit():
            yell[monkey] = float(line[1])
        else:
            op = line[2]
            a = line[1]
            b = line[3]
            yell[monkey] = [a, b, op]
    yell["root"][2] = "="

    yellsHumn("root")
    rootMonkeyYell = yell["root"]
    if yellsHumnMap[rootMonkeyYell[0]]:
        y = getYell(rootMonkeyYell[1])
        print(compute(rootMonkeyYell[0], y))
    else:
        y = getYell(rootMonkeyYell[0])
        print(compute(rootMonkeyYell[1], y))